from __future__ import annotations

import logging
from collections.abc import Sequence
from enum import Enum
from typing import Any, NotRequired, TypedDict

import requests
from rest_framework import status
from sentry_sdk import Scope

from sentry import options
from sentry.integrations.services.integration import integration_service
from sentry.integrations.types import IntegrationProviderSlug
from sentry.integrations.utils.stacktrace_link import RepositoryLinkOutcome
from sentry.models.organization import Organization
from sentry.models.repository import Repository

LineCoverage = Sequence[tuple[int, int]]
CODECOV_REPORT_URL = (
    "https://api.codecov.io/api/v2/{service}/{owner_username}/repos/{repo_name}/file_report/{path}"
)
CODECOV_REPOS_URL = "https://api.codecov.io/api/v2/{service}/{owner_username}"
CODECOV_TIMEOUT = 5

logger = logging.getLogger(__name__)


class CodecovIntegrationError(Enum):
    MISSING_TOKEN = "Internal Error"
    MISSING_GH = "Codecov access can only be enabled if the organization has a GitHub integration."
    MISSING_CODECOV = (
        "Codecov access can only be enabled if the organization has a Codecov integration."
    )


def codecov_enabled(organization: Organization) -> bool:
    # We only need to check the organization flag since the flag will not be set if the plan-based feature flag is False.
    return bool(organization.flags.codecov_access)


def has_codecov_integration(organization: Organization) -> tuple[bool, str | None]:
    """
    Checks if the organization has a Codecov integration.

    Returns a tuple of (has_codecov_integration, error_message)
    """
    integrations = integration_service.get_integrations(
        organization_id=organization.id, providers=[IntegrationProviderSlug.GITHUB.value]
    )
    if not integrations:
        logger.info(
            "codecov.get_integrations",
            extra={"error": "Missing github integration", "org_id": organization.id},
        )
        return False, CodecovIntegrationError.MISSING_GH.value

    for integration in integrations:
        integration_installation = integration.get_installation(organization.id)
        if not integration_installation:
            continue

        repos = integration_installation.get_client().get_repos()
        if not repos:
            continue

        owner_username, _ = repos[0].get("full_name").split("/")
        url = CODECOV_REPOS_URL.format(
            service=IntegrationProviderSlug.GITHUB.value, owner_username=owner_username
        )
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(
                "codecov.check_integration_success",
                extra={"url": url, "org_id": organization.id, "status_code": 200},
            )
            return True, None  # We found a codecov integration, so we can stop looking

        logger.warning(
            "codecov.check_integration_failed",
            extra={"url": url, "status_code": response.status_code, "org_id": organization.id},
        )

    # None of the Github Integrations had a Codecov integration
    return (
        False,
        CodecovIntegrationError.MISSING_CODECOV.value,
    )


def get_codecov_data(repo: str, service: str, path: str) -> tuple[LineCoverage | None, str | None]:
    codecov_token = options.get("codecov.client-secret")
    if not codecov_token:
        return None, None

    owner_username, repo_name = repo.split("/")
    service = "gh" if service == IntegrationProviderSlug.GITHUB.value else service

    path = path.lstrip("/")
    url = CODECOV_REPORT_URL.format(
        service=service,
        owner_username=owner_username,
        repo_name=repo_name,
        path=path,
    )

    line_coverage, codecov_url = None, None
    scope = Scope.get_isolation_scope()

    response = requests.get(
        url,
        params={"walk_back": 10},
        headers={"Authorization": f"Bearer {codecov_token}"},
        timeout=CODECOV_TIMEOUT,
    )
    response.raise_for_status()

    tags = {
        "codecov.request_url": url,
        "codecov.request_path": path,
        "codecov.http_code": response.status_code,
    }

    response_json = response.json()

    tags["codecov.new_endpoint"] = True
    line_coverage = response_json.get("line_coverage")

    coverage_found = line_coverage not in [None, [], [[]]]
    codecov_url = response_json.get("commit_file_url", "")
    tags.update(
        {
            "codecov.coverage_found": coverage_found,
            "codecov.coverage_url": codecov_url,
        },
    )

    for key, value in tags.items():
        scope.set_tag(key, value)

    return line_coverage, codecov_url


class CodecovConfig(TypedDict):
    repository: Repository
    # Config is a serialized RepositoryProjectPathConfig
    config: Any
    outcome: RepositoryLinkOutcome


class CodecovData(TypedDict):
    lineCoverage: NotRequired[LineCoverage]
    coverageUrl: NotRequired[str]
    status: NotRequired[int]
    attemptedUrl: NotRequired[str]


def fetch_codecov_data(config: CodecovConfig) -> CodecovData:
    data: CodecovData = {}
    try:
        # Check if there's an error in the outcome or if sourcePath is missing
        if "error" in config["outcome"] or "sourcePath" not in config["outcome"]:
            data = {"status": status.HTTP_400_BAD_REQUEST}
            return data

        repo = config["repository"].name
        service = config["config"]["provider"]["key"]
        path = config["outcome"]["sourcePath"]

        lineCoverage, codecovUrl = get_codecov_data(repo, service, path)
        if lineCoverage and codecovUrl:
            data = {
                "lineCoverage": lineCoverage,
                "coverageUrl": codecovUrl,
                "status": status.HTTP_200_OK,
            }
    except requests.exceptions.HTTPError as error:
        data = {
            "attemptedUrl": error.response.url,
            "status": error.response.status_code,
        }

        # Do not report an error when coverage is not found
        if error.response.status_code != status.HTTP_404_NOT_FOUND:
            logger.exception("Codecov HTTP error: %s", error.response.status_code)
    except requests.Timeout:
        scope = Scope.get_isolation_scope()
        scope.set_tag("codecov.timeout", True)
        scope.set_tag("codecov.timeout_secs", CODECOV_TIMEOUT)
        scope.set_tag("codecov.http_code", status.HTTP_408_REQUEST_TIMEOUT)
        data = {"status": status.HTTP_408_REQUEST_TIMEOUT}
    except Exception as error:
        data = {"status": status.HTTP_500_INTERNAL_SERVER_ERROR}
        logger.exception(str(error))

    return data
