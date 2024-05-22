<template>
  <tr>
    <!-- 상품 정보 표시 -->
    <td>{{ product.dcls_month }}</td>
    <td>{{ product.kor_co_nm }}</td>
    <td>{{ product.installment_name }}</td>
    <!-- 옵션 금리 표시 -->
    <td>{{ product }}</td>
    <td><button @click="productDetail">Detail</button></td>
  </tr>
</template>

<script setup>
const props = defineProps({
  product:Object,
})
import { useProductStore } from '@/stores/productstore';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const productStore = useProductStore()
const options = ref([])
const router = useRouter()

const productDetail = function () {
  router.push({name: 'installmentdetail', params:{installmentId: props.product.id}})
}

onMounted(() => {
  options.value = productStore.installmentOptions.filter((option) => 
  option.product === props.product.id && option.save_trm >= 6)
  while (options.value.length < 4) {
    options.value.push({intr_rate: '-'})
  }
})
</script>

<style scoped>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>