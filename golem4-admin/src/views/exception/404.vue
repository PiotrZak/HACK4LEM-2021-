<template>
  <a-result status="404" title="404" sub-title="Przykro nam ale podana strona nie istnieje :<">
    <template #extra>
      <a-button type="primary" @click="toHome">
        Powrót do strony głownej
      </a-button>
    </template>
  </a-result>
</template>

<script>
export default {
  name: 'Exception404',
  methods: {
    toHome () {
      this.$router.push({ path: '/' })
    }
  }
}
</script>
