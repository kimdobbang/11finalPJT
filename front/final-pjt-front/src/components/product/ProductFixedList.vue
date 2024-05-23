<template>
  <div class="container">
    <h3>정기예금 목록</h3>
    <div>
      <ProductSearchForm 
      :productType="1"
      @searchClick="searchClick"
      />
    </div>
    <table class="sortable table table-primary table-striped text-center">
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
        <ProductFixedListItem
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
import ProductFixedListItem from '@/components/product/ProductFixedListItem.vue';
import ProductSearchForm from '@/components/product/ProductSearchForm.vue';

const productStore = useProductStore()
const productList = ref([])
const getRateType = ref('')

const searchClick = function (bankType,bankName,rateType) {
  if (bankType == 1) {
    productList.value = productStore.fixedList.filter((product) => product.fin_grp_no == 1)
  } else if (bankType == 2) {
    productList.value = productStore.fixedList.filter((product) => product.fin_grp_no == 2)
  }
  if (bankName) {
    productList.value = productList.value.filter((product) => product.kor_co_nm === bankName)
  }
  if (rateType) {
    getRateType.value = rateType
  }

}

onMounted(() => {
  productStore.getFixed()
  productList.value = productStore.fixedList.filter((product) => product.fin_grp_no == 1)
})
</script>

<style scoped>
@font-face {
  font-family: 'Orbit-Regular';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2310@1.0/Orbit-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
* {
  font-family: 'Orbit-Regular';
  font-size: 20px;
}
</style>