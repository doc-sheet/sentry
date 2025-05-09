import type {EventTransaction} from 'sentry/types/event';
import type {Organization} from 'sentry/types/organization';
import {useApiQuery} from 'sentry/utils/queryClient';
import type {TraceTree} from 'sentry/views/performance/newTraceDetails/traceModels/traceTree';
import type {TraceTreeNode} from 'sentry/views/performance/newTraceDetails/traceModels/traceTreeNode';

interface UseTransactionProps {
  node: TraceTreeNode<TraceTree.Transaction> | null;
  organization: Organization;
}

export function useTransaction(props: UseTransactionProps) {
  return useApiQuery<EventTransaction>(
    [
      `/organizations/${props.organization.slug}/events/${props.node?.value?.project_slug}:${props?.node?.value.event_id}/`,
      {
        query: {
          referrer: 'trace-details-summary',
        },
      },
    ],
    {
      // 10 minutes
      staleTime: 1000 * 60 * 10,
      enabled: !!props.node?.value?.project_slug && !!props.node?.value.event_id,
    }
  );
}
