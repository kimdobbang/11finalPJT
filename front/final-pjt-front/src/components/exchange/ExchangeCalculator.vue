<template>
  <div class="d-flex flex-column justify-content-center align-items-center mt-5">
    <div class="container d-flex flex-column justify-content-center align-items-center mt-4 mb-3">
      <h2>환율계산기</h2>
      <p>원화를 입력해 외화를 계산하세요!</p>
    </div>

      <div class="d-flex flex-column justify-content-center align-items-center">
      <div class="floating mb-4">
        <label for="currency" id="">화폐 선택</label>
        <select v-model="selectedCurrency" @change="selectRate" id="currency" class="form-select">
          <option value="화폐" selected disabled>화폐</option>
          <option v-for="allexchangerate in store.allexchangerates" :key="allexchangerate.CUR_UNIT" :value="allexchangerate">{{ allexchangerate.CUR_NM }}</option>
        </select> 
      </div>

      <div class="d-flex justify-content-center align-items-center">
        <div class="form-floating my-1">
          <input type="text" class="form-control" id="won" placeholder="원화 입력" v-model.trim="won" @input="convertToForex">
          <label for="won">원화</label>
        </div>
        <p class="mx-4" style="text-align: center;"> ↔ </p>
        <div class="form-floating my-1">
          <input type="text" class="form-control" id="forex" placeholder="외화 입력" v-model.trim="forex" @input="convertToWon">
          <label for="forex">{{ selectedCurrency?.CUR_NM }}</label>
        </div>
      </div>
      </div>

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
* {
 font-family: 'Orbit-Regular';
}
h2,p {
  font-family: 'GamtanRoad Batang';
}
</style>