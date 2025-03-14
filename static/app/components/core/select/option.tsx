import {Fragment} from 'react';
import {ClassNames} from '@emotion/react';
import styled from '@emotion/styled';

import type {components as selectComponents} from 'sentry/components/forms/controls/reactSelectWrapper';
import MenuListItem from 'sentry/components/menuListItem';
import {IconAdd, IconCheckmark} from 'sentry/icons';
import {defined} from 'sentry/utils';

type Props = React.ComponentProps<typeof selectComponents.Option>;

export function SelectOption(props: Props) {
  const {
    label,
    data,
    selectProps,
    isMulti,
    isSelected,
    isFocused,
    isDisabled,
    innerProps,
    innerRef,
  } = props;
  const {showDividers, size} = selectProps;
  const {value, selectionMode, priority, ...itemProps} = data;

  const isMultiple = defined(selectionMode) ? selectionMode === 'multiple' : isMulti;

  // Unless the priority prop is explicitly defined, use 'primary' for
  // selected items in single-selection menus and 'default' for the rest.
  const itemPriority = priority ?? (isSelected && !isMultiple ? 'primary' : 'default');

  return (
    <ClassNames>
      {({cx}) => (
        <MenuListItem
          {...itemProps}
          {...innerProps}
          role={isMultiple ? 'menuitemcheckbox' : 'menuitemradio'}
          aria-checked={isSelected}
          ref={innerRef}
          className={cx({
            option: true,
            'option--is-disabled': isDisabled,
            'option--is-focused': isFocused,
            'option--is-selected': isSelected,
          })}
          as="div"
          value={value}
          label={label}
          disabled={isDisabled}
          isFocused={isFocused}
          showDivider={showDividers}
          priority={itemPriority}
          size={size}
          innerWrapProps={{'data-test-id': value}}
          labelProps={{as: typeof label === 'string' ? 'p' : 'div'}}
          leadingItems={
            itemProps.__isNew__ ? (
              <Fragment>
                <IconAdd size="sm" />
                {data.leadingItems}
              </Fragment>
            ) : (
              <Fragment>
                <CheckWrap isMultiple={isMultiple} isSelected={isSelected}>
                  {isSelected && (
                    <IconCheckmark
                      size={isMultiple ? 'xs' : 'sm'}
                      color={isMultiple ? 'white' : undefined}
                    />
                  )}
                </CheckWrap>
                {data.leadingItems}
              </Fragment>
            )
          }
        />
      )}
    </ClassNames>
  );
}

const CheckWrap = styled('div')<{isMultiple: boolean; isSelected: boolean}>`
  display: flex;
  justify-content: center;
  align-items: center;

  ${p =>
    p.isMultiple
      ? `
      width: 1em;
      height: 1em;
      padding: 1px;
      border: solid 1px ${p.theme.border};
      background: ${p.theme.backgroundElevated};
      border-radius: 2px;
      box-shadow: inset ${p.theme.dropShadowMedium};
      ${
        p.isSelected &&
        `
        background: ${p.theme.purple300};
        border-color: ${p.theme.purple300};
       `
      }
    `
      : `
      width: 1em;
      height: 1.4em;
      padding-bottom: 1px;
    `}
`;
