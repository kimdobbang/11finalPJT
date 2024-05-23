<template>
  <div>
    <h3> 환율계산기
    </h3>
    <form>
      <div>
        <label for="currency" id="">화폐 선택</label>
      <select v-model="selectedCurrency" @change="selectRate" id="currency">
        <option value="화폐" selected disabled>화폐</option>
        <option v-for="allexchangerate in store.allexchangerates" :key="allexchangerate.CUR_UNIT" :value="allexchangerate">{{ allexchangerate.CUR_NM }}</option>
      </select> 
      </div>

      <div>
        <label for="won">원화</label>
        <input v-model.number="won" type="text" id="won" @input="convertToForex">
      </div>
        
      <div>
        <label for="forex">외화</label>
        <input v-model.number="forex" type="text" id="forex" @input="convertToWon">
        <p style="display: inline">{{ selectedCurrency?.CUR_UNIT }}</p>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchangestore'
const store = useExchangeStore()

const won = ref(0)
const forex = ref(0)
// 셀렉터에서 선택한 환율 저장 변수
const selectedCurrency = ref(null)
const rate = ref(0)

// 0) 전체 환율 정보 가져오는 함수 호출
onMounted(() => {
  store.getAllExchangeRates()
})


// 1) 셀렉터에서 선택한 환율 갖고 외화로 환전
const convertToForex = () => {
  if (rate.value > 0) {
    forex.value = (won.value / rate.value).toFixed(2)
  }
} 

// 2) 셀렉터에서 선택한 환율 갖고 원화로 환전
const convertToWon = () => {
  if (rate.value > 0) {
    won.value = (forex.value * rate.value).toFixed(2)
  }
}

// 셀렉터에서 환율이 선택되었을 때 호출되는 함수
const selectRate = () => {
  if (selectedCurrency.value) {
    // 쉼표 제거 후 숫자로 변환
    rate.value = Number(selectedCurrency.value.DEAL_BAS_R.replace(/,/g, ""));
    convertToForex(); // 환율이 변경되면 환전 결과 업데이트
  }
}

</script>

<style scoped>

</style>