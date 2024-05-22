<template>
  <div>
    <h1>Installment List</h1>
    <ProductSearchForm 
    :productType="2"
    @searchClick="searchClick"
    />
    <table class="sortable">
      <thead>
        <tr>
          <th>공시 제출월</th>
          <th>금융회사명</th>
          <th>금융상품명</th>
          <th>6 개월</th>
          <th>12 개월</th>
          <th>24 개월</th>
          <th>36 개월</th>
          <th class="sorttable_nosort">상품상세</th>
        </tr>
      </thead>
      <tbody>
        <ProductInstallmentListItem
        v-for="product in productList"
        :product="product"
        :rateType="getRateType"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/productstore';
import ProductInstallmentListItem from '@/components/product/ProductInstallmentListItem.vue';
import ProductSearchForm from '@/components/product/ProductSearchForm.vue';

const productStore = useProductStore()
const productList = ref([])
const getRateType = ref('')

const searchClick = function (bankType,bankName,rateType) {
  if (bankType == 1) {
    productList.value = productStore.installmentList.filter((product) => product.fin_grp_no == 1)
  } else if (bankType == 2) {
    productList.value = productStore.installmentList.filter((product) => product.fin_grp_no == 2)
  }
  if (bankName) {
    productList.value = productList.value.filter((product) => product.kor_co_nm === bankName)
  }
  if (rateType) {
    getRateType.value = rateType
  }

}

onMounted(() => {
  productStore.getInstallment()
  productList.value = productStore.installmentList.filter((product) => product.fin_grp_no == 1)
})
</script>

<style scoped>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>