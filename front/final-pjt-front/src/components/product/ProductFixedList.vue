<template>
  <div>
    <h1>Fixed List</h1>
    <ul>
      <ProductFixedListItem
      v-for="product in productStore.fixedList"
      :product = "product"
      />
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useProductStore } from '@/stores/productstore';
import ProductFixedListItem from '@/components/product/ProductFixedListItem.vue';

const productStore = useProductStore()

onMounted(() => {
  productStore.getFixed()
})
</script>

<style scoped>

</style>