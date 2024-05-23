<template>
  <div @click="handleClick">
   <!--계산을위해 click이벤트 추가 환율 정보를 표시하는 코드 -->
    <ul>
      <li>{{exchangerate.CUR_NM }} :  ({{ exchangerate.CUR_UNIT }}) {{ exchangerate.DEAL_BAS_R }}</li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  exchangerate: Object
})


</script>

<style lang="scss" scoped>

</style>