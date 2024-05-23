<template>
  <div>
    <div class="container d-flex flex-column justify-content-center align-items-center mt-4">
      <h1>주요 화폐 환율</h1>
    </div>
    <div class="d-flex flex-column">
      <p class="mb-0">주요 10개국 환율 (단위: 1원 당)</p>
      <div class="info">
        <ExchangeInfoItem
        v-for="exchangerate in store.exchangerates"
        :key="exchangerate.id"
        :exchangerate="exchangerate"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useExchangeStore } from '@/stores/exchangestore'
import ExchangeInfoItem from '@/components/exchange/ExchangeInfoItem.vue'


const store = useExchangeStore()

</script>

<style scoped>
h1 {
  font-family: 'GamtanRoad Batang';
}
a {
  text-decoration: none;
  color: rgb(125, 122, 122);
  margin-left: 20px;
  margin-right: 20px;
}
.container {
  font-family:'GamtanRoad Batang';
  font-size: 25px;
}
p {
  font-family: 'Orbit-Regular';
}
.info {
  font-family: 'Orbit-Regular';
  width: 100%;
  display: flex;
  flex-flow: row wrap;
  position: relative;
}


</style>