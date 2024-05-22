<template>
  <div>
    <h3> 원하는 환율 선택하거나, 위에서 선택
    </h3>
    <form>
      <label for="won">원화</label>
      <input v-model.number="won" type="text" id="won" @input="convertToForex">
      <p>↕</p>
      <select name="화폐" id=""></select>
      <label for="forex">외화</label>
      <input v-model.number="forex" type="text" id="forex" @input="convertToWon">
      <p>CUR_UNIT -> 이게 외화 옆에 표시되도록</p>
    </form>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

//계산
const props = defineProps({
  rate: {
    type: Number,
    required: true
  }
})

const won = ref(0)
const forex = ref(0)

// 1) 외화로 환전
const convertToForex = () => {
  if (props.rate > 0) {
    forex.value = (won.value / props.rate).toFixed(2)
  }
}

// 2) 원화로 환전
const convertToWon = () => {
  if (props.rate > 0) {
    won.value = (forex.value * props.rate).toFixed(2)
  }
}

// 3) 주요 환율에서 선택된 환율 변경될 때 계산을 다시 수행
watch(() => props.rate, () => {
  convertToForex()
})

// 4)  드롭다운에서 환폐 단위 변경시

</script>

<style scoped>

</style>