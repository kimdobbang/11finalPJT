<template>
  <div>
    <h3>주요 화폐 환율조회</h3>
    <p>주요 10개국 환율 (단위: 1원 당)</p>
    <ExchangeInfoItem
    v-for="exchangerate in store.exchangerates"
    :key="exchangerate.id"
    :exchangerate="exchangerate"/>

  </div>
</template>

<script setup>
import { useExchangeStore } from '@/stores/exchangestore'
import ExchangeInfoItem from '@/components/exchange/ExchangeInfoItem.vue'


const store = useExchangeStore()

</script>

<style scoped>

</style>