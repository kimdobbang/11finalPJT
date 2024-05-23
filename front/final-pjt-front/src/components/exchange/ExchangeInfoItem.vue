<template>
  <div class="card border-success text-center mb-3 item" @click="handleClick">
   <!--계산을위해 click이벤트 추가 환율 정보를 표시하는 코드 -->
   <div class="card-header">{{exchangerate.CUR_NM }}({{ exchangerate.CUR_UNIT }})</div>
    <div class="card-body text-success">
      <p class="card-text">{{ exchangerate.DEAL_BAS_R }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  exchangerate: Object
})


</script>

<style scoped>
.item {
  margin: 4px;
  flex: 0 1 calc(20% - 8px); /* <-- adjusting for margin */
}
</style>