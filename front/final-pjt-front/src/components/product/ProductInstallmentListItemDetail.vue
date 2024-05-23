<template>
  <div>
    <RouterLink :to="{name:'installment'}">[BACK]</RouterLink>
  </div>
  <div v-if="product">
    <p>상품 코드 : {{ product.installment_code }}</p>
    <p>상품 이름 : {{ product.installment_name }}</p>
  </div>
  <form @submit.prevent="joinOutProduct">
    <input type="submit" v-model="userChange">
  </form>
</template>

<script setup>
import { useRoute, useRouter, RouterLink } from 'vue-router';
import { useProductStore } from '@/stores/productstore';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted,ref,watch } from 'vue';
import axios from 'axios';

const productStore = useProductStore()
const accountStore = useAccountStore()
const route = useRoute()
const router = useRouter()
const product = ref({})
product.value = productStore.installmentList.filter((installment) => installment.id == route.params.installmentId)[0]
const userInfo = accountStore.userNow
const productId = product.value.id
const userChange = ref('')

const joinOutProduct = function () {
  if (userChange.value === '가입하기') {
    axios({
      method: 'post',
      url: `${productStore.BASE_URL}/products/installment/${userInfo.username}/${productId}/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      console.log('가입 완료!')
      console.log(`${product.value.installment_name}`)
      alert(`${product.value.installment_name} 상품가입이 완료되었습니다!`)
      accountStore.userNow = res.data
      userChange.value = '탈퇴하기'
    })
  } else {
    axios({
    method: 'delete',
    url: `${productStore.BASE_URL}/products/installment/${userInfo.username}/${productId}/`,
    headers: {
      Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      console.log('탈퇴 완료!')
      accountStore.userNow = res.data
      userChange.value = '가입하기'
    })
  }
} 

onMounted(() => {
  if (userInfo.installment.includes(productId)) {
    userChange.value = '탈퇴하기'
  } else {
    userChange.value = '가입하기'
  }
})
</script>

<style scoped>

</style>