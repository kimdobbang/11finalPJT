<template>
  <tr>
    <!-- 상품 정보 표시 -->
    <td>{{ product.dcls_month }}</td>
    <td>{{ product.kor_co_nm }}</td>
    <td>{{ product.installment_name }}</td>
    <!-- 옵션 금리 표시 -->
    <td v-for="option in filteredOptions">{{ option }}</td>
    <td><button @click="productDetail">Detail</button></td>
  </tr>
</template>

<script setup>
const props = defineProps({
  product:Object,
  rateType:String
})
import { useProductStore } from '@/stores/productstore';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const productStore = useProductStore()
const options = ref([])
const terms = ref(['6','12','24','36'])
const filteredOptions = ref([])
const router = useRouter()
const rateType = props.rateType

const productDetail = function () {
  router.push({name: 'installmentdetail', params:{installmentId: props.product.id}})
}

onMounted(() => {
  if (!rateType) {
    options.value = productStore.installmentOptions.filter((option) => 
    option.product === props.product.id)
  } else if (rateType === '단리') {
    options.value = productStore.installmentOptions.filter((option) => 
    option.product === props.product.id && option.intr_rate_type_nm === '단리')
  } else if (rateType === '복리') {
    options.value = productStore.installmentOptions.filter((option) => 
    option.product === props.product.id && option.intr_rate_type_nm === '복리')
  }
  for (const term of terms.value) {
    let condition = options.value.filter((option) => option.save_trm == term) 
    if (condition.length) {
      filteredOptions.value.push(condition[0].intr_rate)
    } else {
      filteredOptions.value.push('-')
    }
  }
})
</script>

<style scoped>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>