<template>
  <div class="d-flex flex-column justify-content-center align-items-center text-center mt-5" style="width: 80%;">
    <div class="d-flex justify-content-center align-items-center mb-5">
      <ProductSearchForm 
      :productType="2"
      @searchClick="searchClick"
      />
    </div>
    <div>
      <table class="sortable table table-striped text-center" style="border-radius: 5px;">
        <thead>
          <tr>
            <th>공시 제출월</th>
            <th>금융회사명</th>
            <th>금융상품명</th>
            <th>6 개월</th>
            <th>| 12 개월</th>
            <th>| 24 개월</th>
            <th>| 36 개월</th>
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
@font-face {
  font-family: 'Orbit-Regular';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2310@1.0/Orbit-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
* {
  font-family: 'Orbit-Regular';
  font-size: 18px;
}
table {
  border-collapse: collapse;
  box-shadow: 4px 4px 10px 0 rgba(0, 0, 0, 0);
}
table.sortable thead {
    font-weight: bold;
    cursor: pointer;
}
th {
  background-color:  rgba(0, 0, 0, 0.792);
  color: whitesmoke;
}
tbody tr:nth-child(even) {
  background-color: #B4BDFF;
}
</style>