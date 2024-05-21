<template>
  <div v-if="product">
    <p>상품 코드 : {{ product.fixed_code }}</p>
    <p>상품 이름 : {{ product.fixed_name }}</p>
  </div>
  <div>
    <button @click="joinProduct">가입하기</button>
    <button @click="outProduct">탈퇴하기</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useProductStore } from '@/stores/productstore';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted,ref } from 'vue';
import axios from 'axios';

const productStore = useProductStore()
const accountStore = useAccountStore()
const route = useRoute()
const product = ref({})
product.value = productStore.fixedList.filter((fixed) => fixed.id == route.params.fixedId)[0]

const joinProduct = function () {
  axios({
    method: 'post',
    url: `${productStore.BASE_URL}/products/fixed/:username/:productId`,
    params: {
      username: accountStore.userNow.username,
      productId: product.id
    },
    headers: {
      Authorization: `Token ${accountStore.TOKEN}`
    }
  })
  .then(res => {
    console.log('가입 완료!')
    accountStore.userNow = res.data
  })
}
onMounted(() =>{
})

</script>

<style scoped>

</style>