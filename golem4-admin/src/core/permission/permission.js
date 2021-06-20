export const PERMISSION_ENUM = {
  'add': { key: 'add', label: 'dodaj' },
  'delete': { key: 'delete', label: 'usuń' },
  'edit': { key: 'edit', label: 'edytuj' },
  'query': { key: 'query', label: 'odszukaj' },
  'get': { key: 'get', label: 'wczytaj' },
  'enable': { key: 'enable', label: 'włącz' },
  'disable': { key: 'disable', label: 'wyłącz' },
  'import': { key: 'import', label: 'importuj' },
  'export': { key: 'export', label: 'eksportuj' }
}

/**
 * <a-button v-if="$auth('form.edit')">Button</a-button>
 * @param Vue
 */
function plugin (Vue) {
  if (plugin.installed) {
    return
  }

  !Vue.prototype.$auth && Object.defineProperties(Vue.prototype, {
    $auth: {
      get () {
        const _this = this
        return (permissions) => {
          const [permission, action] = permissions.split('.')
          const permissionList = _this.$store.getters.roles.permissions
          return permissionList.find((val) => {
            return val.permissionId === permission
          }).actionList.findIndex((val) => {
            return val === action
          }) > -1
        }
      }
    }
  })

  !Vue.prototype.$enum && Object.defineProperties(Vue.prototype, {
    $enum: {
      get () {
        // const _this = this;
        return (val) => {
          let result = PERMISSION_ENUM
          val && val.split('.').forEach(v => {
            result = result && result[v] || null
          })
          return result
        }
      }
    }
  })
}

export default plugin
