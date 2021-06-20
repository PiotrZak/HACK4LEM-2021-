<template>
  <a-list itemLayout="horizontal">
    <a-list-item>
      <a-list-item-meta>
        <template v-slot:title>
          <a>Agrogator</a>
        </template>
        <template v-slot:description>
          <span>
            Auto AI
          </span>
        </template>
      </a-list-item-meta>
      <template v-slot:actions>
        <a-switch checkedChildren="暗色" unCheckedChildren="白色" :defaultChecked="navTheme === 'dark' && true || false" @change="onChange" />
      </template>
    </a-list-item>
    <a-list-item>
      <a-list-item-meta>
        <template v-slot:title>
          <a>Skanowanie</a>
        </template>
        <template v-slot:description>
          <span>
            Poziom skanowania: Najwyzszy poziom
          </span>
        </template>
      </a-list-item-meta>
    </a-list-item>
  </a-list>
</template>
<script>
import { colorList } from '@/components/SettingDrawer/settingConfig'
import { baseMixin } from '@/store/app-mixin'
import { NAV_THEME, TOGGLE_NAV_THEME } from '@/store/mutation-types'

const themeMap = {
  'dark': 'dark',
  'light': 'light'
}

export default {
  mixins: [baseMixin],
  data () {
    return {
    }
  },
  filters: {
    themeFilter (theme) {
      return themeMap[theme]
    }
  },
  methods: {
    colorFilter (color) {
      const c = colorList.find(o => o.color === color)
      return c && c.key
    },

    onChange (checked) {
      if (checked) {
        this.$store.commit(TOGGLE_NAV_THEME, NAV_THEME.DARK)
      } else {
        this.$store.commit(TOGGLE_NAV_THEME, NAV_THEME.LIGHT)
      }
    }
  }
}
</script>
