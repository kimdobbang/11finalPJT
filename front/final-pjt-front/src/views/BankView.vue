<template>
  <div>
    <BankSearchForm @update:keyword="updateKeyword" />
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
/* 필요한 스타일 추가 */
</style>
