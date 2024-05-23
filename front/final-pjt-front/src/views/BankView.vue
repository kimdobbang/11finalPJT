<template>
  <div class="container d-flex flex-column justify-content-center align-items-center mt-4">
    <h1>주변 은행 찾기</h1>
  </div>
  <div class="container d-flex justify-content-center align-items-center">
    <BankSearchForm @update:keyword="updateKeyword" />
  </div>
  <div class="container d-flex justify-content-center align-items-center mt-5">
    <BankMap :keyword="keyword" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import BankSearchForm from '@/components/bank/BankSearchForm.vue'
import BankMap from '@/components/bank/BankMap.vue'

const keyword = ref('')

const updateKeyword = (newKeyword) => {
  keyword.value = newKeyword
}
</script>

<style scoped>
a{
  text-decoration: none;
  color: rgb(125, 122, 122);
  margin-left: 20px;
  margin-right: 20px;
}
.container {
  font-family:'GamtanRoad Batang';
  font-size: 20px;
}
.nav-link:hover {
  color: #83A2FF;
}
</style>
