<template>
  <div>
    <h3>주요 화폐 환율조회</h3>
    <p>주요 10개국 환율 (단위: 1원 당)</p>
    <ExchangeInfoItem
    v-for="exchangerate in store.exchangerates"
    :key="exchangerate.id"
    :exchangerate="exchangerate"
    @click="selectRate(exchangerate.DEAL_BAS_R)"/>

<!-- @click 이벤트로 계산할 환율 선택 -->
  </div>
</template>

<script setup>
import { defineEmits } from 'vue'
import { useExchangeStore } from '@/stores/exchangestore'
import ExchangeInfoItem from '@/components/exchange/ExchangeInfoItem.vue'


const store = useExchangeStore()
//계산기
const emit = defineEmits(['rate-selected'])
const selectRate = (rate) => {
  emit('rate-selected', rate)
}
//계산끝
</script>

<style scoped>

</style>