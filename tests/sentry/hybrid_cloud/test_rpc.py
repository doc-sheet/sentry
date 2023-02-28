from django.test import override_settings

from sentry.services.hybrid_cloud.organization import (
    OrganizationService,
    RpcOrganizationMemberFlags,
)
from sentry.services.hybrid_cloud.organization.impl import DatabaseBackedOrganizationService
from sentry.services.hybrid_cloud.user import RpcUser
from sentry.silo import SiloMode
from sentry.testutils import TestCase


class RpcServiceTest(TestCase):
    def test_remote_service(self):
        user = self.create_user()
        organization = self.create_organization()

        serial_user = RpcUser(id=user.id)
        serial_org = DatabaseBackedOrganizationService.serialize_organization(organization)

        with override_settings(SILO_MODE=SiloMode.CONTROL):
            service = OrganizationService.resolve_to_delegation()

            # TODO: Handle forward refs in service method definitions
            service.add_organization_member(
                organization=serial_org,
                user=serial_user,
                flags=RpcOrganizationMemberFlags(),
                role=None,
            )
