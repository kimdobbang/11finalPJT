<template>
  <div>
    <h2>가까운 은행 찾기</h2>
  </div>
  <div>
    <BankSearchForm />
    <br><br>
    <BankMap />
  </div>
</template>

<script setup>
import BankSearchForm from '@/components/bank/BankSearchForm.vue';
import BankMap from '@/components/bank/BankMap.vue' ;

</script>

<style scoped>

</style>