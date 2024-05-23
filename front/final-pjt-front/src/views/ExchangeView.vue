<template>
  <div class="container">
    <ExchangeInfo @rate-selected="updateRate" />
  </div>
  <div class="container">
    <ExchangeCalculator :rate="selectedRate" />
  </div>
  <!-- 계산 하려면 @rate-selected, :rate 쓰라고 함 지피티가 -->
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchangestore'
import ExchangeInfo from '@/components/exchange/ExchangeInfo.vue'
import ExchangeCalculator from '@/components/exchange/ExchangeCalculator.vue'


// 컴포넌트가 마운트될 때 환율 정보를 가져오는 함수 호출 (환율 최신을 어떻게 유지? get말고 put?)
const store = useExchangeStore()
onMounted(() => {
  store.getExchangeRates()
})


//계산기
// 선택된 환율을 저장하는 상태 변수
const selectedRate = ref(0)

// 환율이 선택되었을 때 호출되는 함수
const updateRate = (rate) => {
  selectedRate.value = rate
}
//계산기

</script>

<style scoped>

</style>