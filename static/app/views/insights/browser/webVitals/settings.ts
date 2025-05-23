import {t} from 'sentry/locale';

export const MODULE_TITLE = t('Web Vitals');
export const BASE_URL = 'pageloads';
export const DATA_TYPE = t('Web Vitals');
export const DATA_TYPE_PLURAL = t('Web Vitals');

export const MODULE_DOC_LINK =
  'https://docs.sentry.io/product/insights/frontend/web-vitals/';

export const DEFAULT_QUERY_FILTER =
  'transaction.op:[pageload,""] span.op:[ui.interaction.click,ui.interaction.hover,ui.interaction.drag,ui.interaction.press,ui.webvital.cls,""] !transaction:"<< unparameterized >>"';

export const DEFAULT_EAP_QUERY_FILTER =
  'span.op:[ui.interaction.click,ui.interaction.hover,ui.interaction.drag,ui.interaction.press,ui.webvital.cls,pageload,""] !transaction:"<< unparameterized >>"';

export const MODULE_FEATURES = ['insights-initial-modules'];
