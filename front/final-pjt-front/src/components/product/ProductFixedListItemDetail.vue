<template>
  <div>
    <RouterLink :to="{name:'fixed'}">[BACK]</RouterLink>
  </div>
  <div v-if="product">
    <p>상품 코드 : {{ product.fixed_code }}</p>
    <p>상품 이름 : {{ product.fixed_name }}</p>
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
product.value = productStore.fixedList.filter((fixed) => fixed.id == route.params.fixedId)[0]
const userInfo = accountStore.userNow
const productId = product.value.id
const userChange = ref('')

const joinOutProduct = function () {
  if (userChange.value === '가입하기') {
    axios({
      method: 'post',
      url: `${productStore.BASE_URL}/products/fixed/${userInfo.username}/${productId}/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      console.log('가입 완료!')
      console.log(`${product.value.fixed_name}`)
      alert(`${product.value.fixed_name} 상품가입이 완료되었습니다!`)
      accountStore.userNow = res.data
      userChange.value = '탈퇴하기'
    })
  } else {
    axios({
    method: 'delete',
    url: `${productStore.BASE_URL}/products/fixed/${userInfo.username}/${productId}/`,
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
  if (userInfo.fixed.includes(productId)) {
    userChange.value = '탈퇴하기'
  } else {
    userChange.value = '가입하기'
  }
})
</script>

<style scoped>

</style>