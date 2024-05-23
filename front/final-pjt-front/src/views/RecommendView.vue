<template>
  <div class="d-flex w-100 h-100 justify-content-center">
    <GPT />
    <div class="d-flex flex-column mt-auto w-50 h-100">
      <div class="mt-3">
        <h3>예/적금 추천받기</h3>
      </div>
      <button @click="recommendProduct" class="join">추천받기</button>
      <div class="card my-3 w-75 text-bg-success">
        <div class="card-header" style="font-weight: bold;">추천받으신 예금상품</div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item" v-for="product in recommendFixed">{{ product.kor_co_nm }} - {{ product.fixed_name }}</li>
        </ul>
      </div>
      <div class="card my-3 w-75 text-bg-warning">
        <div class="card-header" style="font-weight: bold;">추천받으신 적금상품</div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item" v-for="product in recommendInstallment">{{ product.kor_co_nm }} - {{ product.installment_name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import GPT from '@/components/chatbot/GPT.vue'
import axios from 'axios';
import { useAccountStore } from '@/stores/accountstore';
import { ref } from 'vue';

const accountStore = useAccountStore()
const username = accountStore.userNow.username
const recommendList = ref([])
const recommendFixed = ref([])
const recommendInstallment = ref([])
const recommendProduct = function () {
  axios({
    method:'get',
    url:`${accountStore.BASE_URL}/products/recommend/${username}/`,
    params: {
      username:username
    }
  })
  .then(res => {
    recommendFixed.value = res.data.recommended_fixed
    recommendInstallment.value = res.data.recommended_installment
  })
  .catch(err => console.log(err))
}


</script>

<style scoped>
* {
 font-family: 'Orbit-Regular';
}
h3 {
  font-family: 'GamtanRoad Batang';
}
.join {
  width: 30%;
  height: 40px;
  border: 0px;
  border-radius: 40px;
  margin-top: 20px;
  background-color: rgb(131, 162, 255);
  font-family: 'KCC-Hanbit';
  font-size: 20px;
  color: whitesmoke;
}
.join:hover {
  background-color:rgb(180, 189, 255);
  transition: 0.5s;
}
.join:active {
  background-color: rgb(133, 140, 188);
  box-shadow: inset 3px 3px 3px 3px  rgb(166, 175, 235);
  transition: 0.2s;
}
</style>