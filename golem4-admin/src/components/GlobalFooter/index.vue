<template>
  <global-footer class="footer custom-render">
    <template v-slot:links>
      <a href="https://hack4lem.com/" target="_blank">Hack4Lem</a>
    </template>
    <template v-slot:copyright>
      <a href="https://github.com/PiotrZak/lem-golem" target="_blank">-= GolemIV Team =-</a>
    </template>
  </global-footer>
</template>

<script>
import { GlobalFooter } from '@ant-design-vue/pro-layout'

export default {
  name: 'ProGlobalFooter',
  components: {
    GlobalFooter
  }
}
</script>
