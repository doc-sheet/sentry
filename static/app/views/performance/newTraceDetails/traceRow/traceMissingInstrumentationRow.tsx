import {t} from 'sentry/locale';
import {TraceIcons} from 'sentry/views/performance/newTraceDetails/traceIcons';
import type {TraceTree} from 'sentry/views/performance/newTraceDetails/traceModels/traceTree';
import type {TraceTreeNode} from 'sentry/views/performance/newTraceDetails/traceModels/traceTreeNode';
import {
  makeTraceNodeBarColor,
  MissingInstrumentationTraceBar,
} from 'sentry/views/performance/newTraceDetails/traceRow/traceBar';
import {
  maybeFocusTraceRow,
  TraceRowConnectors,
  type TraceRowProps,
} from 'sentry/views/performance/newTraceDetails/traceRow/traceRow';

export function TraceMissingInstrumentationRow(
  props: TraceRowProps<TraceTreeNode<TraceTree.MissingInstrumentationSpan>>
) {
  return (
    <div
      key={props.index}
      ref={r =>
        props.tabIndex === 0
          ? maybeFocusTraceRow(r, props.node, props.previouslyFocusedNodeRef)
          : undefined
      }
      tabIndex={props.tabIndex}
      className={`TraceRow ${props.rowSearchClassName}`}
      onPointerDown={props.onRowClick}
      onKeyDown={props.onRowKeyDown}
      style={props.style}
    >
      <div
        className="TraceLeftColumn"
        ref={props.registerListColumnRef}
        onDoubleClick={props.onRowDoubleClick}
      >
        <div className="TraceLeftColumnInner" style={props.listColumnStyle}>
          <div className="TraceChildrenCountWrapper">
            <TraceRowConnectors node={props.node} manager={props.manager} />
          </div>
          <span className="TraceOperation">{t('No Instrumentation')}</span>
        </div>
      </div>
      <div
        ref={props.registerSpanColumnRef}
        className={props.spanColumnClassName}
        onDoubleClick={props.onRowDoubleClick}
      >
        <MissingInstrumentationTraceBar
          virtualized_index={props.virtualized_index}
          manager={props.manager}
          color={makeTraceNodeBarColor(props.theme, props.node)}
          node_space={props.node.space}
        />
        <button
          ref={props.registerSpanArrowRef}
          className="TraceArrow"
          onClick={props.onSpanArrowClick}
        >
          <TraceIcons.Chevron direction="left" />
        </button>
      </div>
    </div>
  );
}
