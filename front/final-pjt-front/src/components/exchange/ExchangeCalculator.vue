<template>
  <div>
    <h3> 원하는 환율 선택하거나, 위에서 선택
    </h3>
    <form>
      <label for="won">원화</label>
      <input v-model.number="won" type="text" id="won" @input="convertToForex">
      <p>↕</p>
       
      <label for="currency" id="">화폐 선택</label>
      <select v-model="selectedCurrency" @change="selectRate" id="currency">
        <option value="화폐" selected disabled>화폐</option>
        <option v-for="allexchangerate in store.allexchangerates" :key="allexchangerate.CUR_UNIT" :value="allexchangerate">{{ allexchangerate.CUR_NM }}</option>
      </select> 
        
      <label for="forex">외화</label>
      <input v-model.number="forex" type="text" id="forex" @input="convertToWon">
      <p style="display: inline">{{ selectedCurrency?.CUR_UNIT }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useExchangeStore } from '@/stores/exchangestore'
const store = useExchangeStore()


const rate = ref(0)
const won = ref(0)
const forex = ref(0)
// 셀렉터에서 선택한 환율 저장 변수
const selectedCurrency = ref(null)

// 셀렉터에서 환율이 선택되었을 때 호출되는 함수
const selectRate = () => {
  if (selectedCurrency.value) {
    rate.value = selectedCurrency.value.DEAL_BAS_R // 선택된 환율로 업데이트
  }
}

// 0) 전체 환율 정보 가져오는 함수 호출
onMounted(() => {
  store.getAllExchangeRates()
})


// 1) 셀렉터에서  선택한 환율 갖고 외화로 환전
const convertToForex = () => {
  if (selectedCurrency.value && rate.value > 0) {
    forex.value = (won.value / rate.value).toFixed(2)
  }
} 

// 2) 셀렉터에서 선택한 환율 갖고 원화로 환전
const convertToWon = () => {
  if (selectedCurrency.value && rate.value > 0) {
    won.value = (forex.value * rate.value).toFixed(2)
  }
}

// 3) 셀렉터에서 선택된 환율 변경될 때 계산을 다시 수행
watch(() => rate.value, () => {
  convertToForex()
})  
watch(() => rate.value, () => {
  convertToWon()
})  


// 4) 셀렉터에서 선택한 함수로 계산 수행

</script>

<style scoped>

</style>