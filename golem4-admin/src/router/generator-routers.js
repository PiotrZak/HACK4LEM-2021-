// eslint-disable-next-line
import * as loginService from '@/api/login'
// eslint-disable-next-line
import { BasicLayout, BlankLayout, PageView, RouteView } from '@/layouts'

const constantRouterComponents = {
  BasicLayout: BasicLayout,
  BlankLayout: BlankLayout,
  RouteView: RouteView,
  PageView: PageView,
  '403': () => import(/* webpackChunkName: "error" */ '@/views/exception/403'),
  '404': () => import(/* webpackChunkName: "error" */ '@/views/exception/404'),
  '500': () => import(/* webpackChunkName: "error" */ '@/views/exception/500'),

  'Workplace': () => import('@/views/dashboard/Workplace'),
  'Analysis': () => import('@/views/dashboard/Analysis'),

  // // form
  // 'BasicForm': () => import('@/views/form/basicForm'),
  // 'StepForm': () => import('@/views/form/stepForm/StepForm'),
  // 'AdvanceForm': () => import('@/views/form/advancedForm/AdvancedForm'),

  // // list
  // 'TableList': () => import('@/views/list/TableList'),
  // 'StandardList': () => import('@/views/list/BasicList'),
  // 'CardList': () => import('@/views/list/CardList'),
  // 'SearchLayout': () => import('@/views/list/search/SearchLayout'),
  // 'SearchArticles': () => import('@/views/list/search/Article'),
  // 'SearchProjects': () => import('@/views/list/search/Projects'),
  // 'SearchApplications': () => import('@/views/list/search/Applications'),
  // 'ProfileBasic': () => import('@/views/profile/basic'),
  // 'ProfileAdvanced': () => import('@/views/profile/advanced/Advanced'),

  // // result
  // 'ResultSuccess': () => import(/* webpackChunkName: "result" */ '@/views/result/Success'),
  // 'ResultFail': () => import(/* webpackChunkName: "result" */ '@/views/result/Error'),

  // exception
  'Exception403': () => import(/* webpackChunkName: "fail" */ '@/views/exception/403'),
  'Exception404': () => import(/* webpackChunkName: "fail" */ '@/views/exception/404'),
  'Exception500': () => import(/* webpackChunkName: "fail" */ '@/views/exception/500'),

  // // account
  // 'AccountCenter': () => import('@/views/account/center'),
  // 'AccountSettings': () => import('@/views/account/settings/Index'),
  // 'BaseSettings': () => import('@/views/account/settings/BaseSetting'),
  // 'SecuritySettings': () => import('@/views/account/settings/Security'),
  // 'CustomSettings': () => import('@/views/account/settings/Custom'),
  // 'BindingSettings': () => import('@/views/account/settings/Binding'),
  // 'NotificationSettings': () => import('@/views/account/settings/Notification')

  // 'TestWork': () => import(/* webpackChunkName: "TestWork" */ '@/views/dashboard/TestWork')
}

const notFoundRouter = {
  path: '*', redirect: '/404', hidden: true
}

const rootRouter = {
  key: '',
  name: 'index',
  path: '',
  component: 'BasicLayout',
  redirect: '/panel',
  meta: {
    title: '首页'
  },
  children: []
}

/**
 * @param token
 * @returns {Promise<Router>}
 */
export const generatorDynamicRouter = (token) => {
  return new Promise((resolve, reject) => {
    loginService.getCurrentUserNav(token).then(res => {
      console.log('res', res)
      const { result } = res
      const menuNav = []
      const childrenNav = []
      listToTree(result, childrenNav, 0)
      rootRouter.children = childrenNav
      menuNav.push(rootRouter)
      console.log('menuNav', menuNav)
      const routers = generator(menuNav)
      routers.push(notFoundRouter)
      console.log('routers', routers)
      resolve(routers)
    }).catch(err => {
      reject(err)
    })
  })
}

/**
 *
 * @param routerMap
 * @param parent
 * @returns {*}
 */
export const generator = (routerMap, parent) => {
  return routerMap.map(item => {
    const { title, show, hideChildren, hiddenHeaderContent, target, icon } = item.meta || {}
    const currentRouter = {
      path: item.path || `${parent && parent.path || ''}/${item.key}`,
      name: item.name || item.key || '',
      // component: constantRouterComponents[item.component || item.key],
      component: (constantRouterComponents[item.component || item.key]) || (() => import(`@/views/${item.component}`)),
      meta: {
        title: title,
        icon: icon || undefined,
        hiddenHeaderContent: hiddenHeaderContent,
        target: target,
        permission: item.name
      }
    }
    if (show === false) {
      currentRouter.hidden = true
    }
    if (hideChildren) {
      currentRouter.hideChildrenInMenu = true
    }
    if (!currentRouter.path.startsWith('http')) {
      currentRouter.path = currentRouter.path.replace('//', '/')
    }
    item.redirect && (currentRouter.redirect = item.redirect)
    if (item.children && item.children.length > 0) {
      // Recursion
      currentRouter.children = generator(item.children, currentRouter)
    }
    return currentRouter
  })
}

/**
 * @param list 
 * @param tree
 * @param parentId
 */
const listToTree = (list, tree, parentId) => {
  list.forEach(item => {
    if (item.parentId === parentId) {
      const child = {
        ...item,
        key: item.key || item.name,
        children: []
      }
      listToTree(list, child.children, item.id)
      if (child.children.length <= 0) {
        delete child.children
      }
      tree.push(child)
    }
  })
}
