import type {Location} from 'history';

import {normalizeDateTimeParams} from 'sentry/components/organizations/pageFilters/parse';
import {ALL_ACCESS_PROJECTS} from 'sentry/constants/pageFilters';
import type {EventTransaction} from 'sentry/types/event';
import type {Organization} from 'sentry/types/organization';
import {MutableSearch} from 'sentry/utils/tokenizeSearch';
import type {TraceItemResponseAttribute} from 'sentry/views/explore/hooks/useTraceItemDetails';
import {makeTracesPathname} from 'sentry/views/traces/pathnames';

export function getProfileMeta(event: EventTransaction | null) {
  const profileId = event?.contexts?.profile?.profile_id;
  if (profileId) {
    return profileId;
  }
  const profilerId = event?.contexts?.profile?.profiler_id;
  if (profilerId) {
    const start = new Date(event.startTimestamp * 1000);
    const end = new Date(event.endTimestamp * 1000);
    return {
      profiler_id: profilerId,
      start: start.toISOString(),
      end: end.toISOString(),
    };
  }
  return null;
}

export enum TraceDrawerActionValueKind {
  TAG = 'tag',
  MEASUREMENT = 'measurement',
  ADDITIONAL_DATA = 'additional_data',
  SENTRY_TAG = 'sentry_tag',
}

export enum TraceDrawerActionKind {
  INCLUDE = 'include',
  EXCLUDE = 'exclude',
  GREATER_THAN = 'greater_than',
  LESS_THAN = 'less_than',
}

export function getSearchInExploreTarget(
  organization: Organization,
  location: Location,
  projectIds: string | string[] | undefined,
  key: string,
  value: string,
  kind: TraceDrawerActionKind
) {
  const {start, end, statsPeriod} = normalizeDateTimeParams(location.query);
  const search = new MutableSearch('');

  if (kind === TraceDrawerActionKind.INCLUDE) {
    search.setFilterValues(key, [value]);
  } else if (kind === TraceDrawerActionKind.EXCLUDE) {
    search.setFilterValues(`!${key}`, [`${value}`]);
  } else if (kind === TraceDrawerActionKind.GREATER_THAN) {
    search.setFilterValues(key, [`>${value}`]);
  } else {
    search.setFilterValues(key, [`<${value}`]);
  }

  return {
    pathname: makeTracesPathname({
      organization,
      path: '/',
    }),
    query: {
      start,
      end,
      statsPeriod,
      query: search.formatString(),
      project: projectIds ? projectIds : ALL_ACCESS_PROJECTS,
    },
  };
}

export function findSpanAttributeValue(
  attributes: TraceItemResponseAttribute[],
  attributeName: string
) {
  return attributes.find(attribute => attribute.name === attributeName)?.value.toString();
}

// Sort attributes so that span.* attributes are at the beginning and
// the rest of the attributes are sorted alphabetically.
export function sortAttributes(attributes: TraceItemResponseAttribute[]) {
  return [...attributes].sort((a, b) => {
    const aIsSpan = a.name.startsWith('span.');
    const bIsSpan = b.name.startsWith('span.');

    if (aIsSpan && !bIsSpan) {
      return -1;
    }
    if (!aIsSpan && bIsSpan) {
      return 1;
    }
    return a.name.localeCompare(b.name);
  });
}
