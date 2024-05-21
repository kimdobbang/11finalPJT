<template>
  <div>
    <h1>Fixed List</h1>
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
        <ProductFixedListItem
        v-for="product in productList"
        :product = "product"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/productstore';
import ProductFixedListItem from '@/components/product/ProductFixedListItem.vue';

const productStore = useProductStore()
const productList = ref([])
const productInfo = ref({})


// 표 정렬
// import { SortTable } from "./sort";
 
// const SORT = new SortTable();
 
// window.addEventListener('click',(e)=>{
//   const target = e.target;
//   if(target.dataset.sort){
//     SORT.onClick(target);
//   }
// });


onMounted(() => {
  productStore.getFixed()
  productList.value = productStore.fixedList
})
</script>

<style scoped>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>