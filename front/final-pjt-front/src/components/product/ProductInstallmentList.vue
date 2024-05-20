<template>
  <div>
    <h1>Installment List</h1>
    <ul>
      <ProductInstallmentListItem
      v-for="product in productStore.installmentList"
      :product = "product"
      />
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useProductStore } from '@/stores/productstore';
import ProductInstallmentListItem from '@/components/product/ProductInstallmentListItem.vue';

const productStore = useProductStore()

onMounted(() => {
  productStore.getInstallment()
})
</script>

<style scoped>

</style>