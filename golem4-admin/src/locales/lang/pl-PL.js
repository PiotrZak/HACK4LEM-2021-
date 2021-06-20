import antd from 'ant-design-vue/es/locale-provider/pl_PL'
import momentCN from 'moment/locale/pl'
import global from './pl-PL/global'

import menu from './pl-PL/menu'
import setting from './pl-PL/setting'
import user from './pl-PL/user'
import dashboard from './pl-PL/dashboard'
import form from './pl-PL/form'
import result from './pl-PL/result'
import account from './pl-PL/account'

const components = {
  antLocale: antd,
  momentName: 'pl-PL',
  momentLocale: momentCN
}

export default {
  message: '-',

  'layouts.usermenu.dialog.title': 'GolemIV',
  'layouts.usermenu.dialog.content': 'Czy chcesz się wylogować?',
  'layouts.userLayout.title': 'Hackaton :: Hack4Lem @ 2021',
  ...components,
  ...global,
  ...menu,
  ...setting,
  ...user,
  ...dashboard,
  ...form,
  ...result,
  ...account
}
