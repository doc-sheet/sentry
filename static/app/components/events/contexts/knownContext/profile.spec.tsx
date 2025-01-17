import {TransactionEventFixture} from 'sentry-fixture/event';
import {OrganizationFixture} from 'sentry-fixture/organization';
import {ProjectFixture} from 'sentry-fixture/project';

import {render, screen} from 'sentry-test/reactTestingLibrary';

import ContextCard from 'sentry/components/events/contexts/contextCard';
import {getProfileContextData} from 'sentry/components/events/contexts/knownContext/profile';

const PROFILE_ID = '61d2d7c5acf448ffa8e2f8f973e2cd36';
const PROFILER_ID = '5e7250f0d25443daa3f59c20835aed31';
const MOCK_PROFILE_CONTEXT = {
  type: 'default',
  profile_id: PROFILE_ID,
  profiler_id: PROFILER_ID,
  // Extra data is still valid and preserved
  extra_data: 'something',
  unknown_key: 123,
};

const MOCK_REDACTION = {
  extra_data: {
    '': {
      rem: [['organization:0', 's', 0, 0]],
      len: 5,
    },
  },
};

describe('ProfileContext', function () {
  const organization = OrganizationFixture();
  const project = ProjectFixture();

  it('returns values and according to the parameters', function () {
    const event = TransactionEventFixture({
      _meta: {contexts: {profile: MOCK_REDACTION}},
    });

    expect(
      getProfileContextData({
        data: MOCK_PROFILE_CONTEXT,
        event,
        organization,
        project,
      })
    ).toEqual([
      {
        key: 'profile_id',
        subject: 'Profile ID',
        value: PROFILE_ID,
        action: {
          link: `/organizations/${organization.slug}/profiling/profile/${project.slug}/${PROFILE_ID}/flamegraph/`,
        },
      },
      {
        key: 'profiler_id',
        subject: 'Profiler ID',
        value: PROFILER_ID,
        action: {
          link: {
            pathname: `/organizations/${organization.slug}/profiling/profile/${project.slug}/flamegraph/`,
            query: {
              profilerId: PROFILER_ID,
              eventId: event.id,
              start: '2023-12-28T15:58:21.000Z',
              end: '2023-12-28T15:58:20.000Z',
            },
          },
        },
      },
      {
        key: 'extra_data',
        subject: 'extra_data',
        value: 'something',
        meta: undefined,
      },
      {
        key: 'unknown_key',
        subject: 'unknown_key',
        value: 123,
        meta: undefined,
      },
    ]);
  });

  it('renders with meta annotations correctly', function () {
    const event = TransactionEventFixture({
      _meta: {contexts: {profile: MOCK_REDACTION}},
    });

    render(
      <ContextCard
        event={event}
        type={'default'}
        alias={'profile'}
        project={project}
        value={{...MOCK_PROFILE_CONTEXT, extra_data: ''}}
      />,
      {organization}
    );

    expect(screen.getByText('Profile')).toBeInTheDocument();
    expect(screen.getByText('Profile ID')).toBeInTheDocument();
    expect(screen.getByRole('link', {name: PROFILE_ID})).toBeInTheDocument();
    expect(screen.getByText('extra_data')).toBeInTheDocument();
    expect(screen.getByText(/redacted/)).toBeInTheDocument();
  });
});
