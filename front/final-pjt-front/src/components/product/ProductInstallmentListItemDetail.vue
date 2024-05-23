<template>
  <div class="d-flex flex-column w-75 justify-content-center align-items-center" >
  <div class="backbtn d-flex justify-content-auto align-items-auto me-auto">
    <RouterLink :to="{name:'installment'}">◀</RouterLink>
  </div>
  <div v-if="product">
    <table class="table table-striped text-center" style="width: 100%;">
      <tbody>
        <tr>
          <th scope="row">상품 코드</th>
          <td colspan="3">{{ product.installment_code }}</td>
        </tr>
        <tr>
          <th scope="row" style="font-weight: bold;">은행명</th>
          <td colspan="3">{{ product.kor_co_nm }}</td>
        </tr>
        <tr>
          <th scope="row" style="font-weight: bold;">상품 이름</th>
          <td colspan="3">{{ product.installment_name }}</td>
        </tr>
        <tr>
          <th scope="row" rowspan="3" style="text-align: center;">가입 정보</th>
          <th scope="row">가입 방법 :</th>
          <td colspan="2">{{ product.join_way }}</td>
        </tr>
        <tr>
          <th scope="row">가입 제한 :</th>
          <td colspan="2">{{ deny[product.join_deny] }}</td>
        </tr>
        <tr>
          <th scope="row">가입 대상 :</th>
          <td colspan="2">{{ product.join_member }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <hr>
  <h1>상품 옵션 리스트</h1>
  <div class="d-flex flex-wrap w-100">
    <div class="col-6 col-md-4 col-lg-3" v-for="option in options">
      <div class="card m-3">
        <div class="card-header">
          {{ option.save_trm }}개월 형
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">저축 금리 유형 : {{ option.intr_rate_type_nm }}</li>
          <li class="list-group-item">저축 금리 : {{ option.intr_rate }}%</li>
          <li class="list-group-item">최고 우대금리 : {{ option.intr_rate }}%</li>
        </ul>
      </div>
    </div>
  </div>
  <form @submit.prevent="joinOutProduct" style="margin-bottom: 20px;">
    <input class="join" type="submit" v-show="userChange==='가입하기'" v-model="userChange">
    <input class="out" type="submit" v-show="userChange==='탈퇴하기'" v-model="userChange">
  </form>
  </div>
</template>

<script setup>
import { useRoute, RouterLink } from 'vue-router';
import { useProductStore } from '@/stores/productstore';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted,ref } from 'vue';
import axios from 'axios';

const productStore = useProductStore()
const accountStore = useAccountStore()
const route = useRoute()
const product = ref({})
const options = ref([])
const deny = ref(['-','제한 없음','서민 전용','일부 제한'])
product.value = productStore.installmentList.filter((installment) => installment.id == route.params.installmentId)[0]
options.value = productStore.installmentOptions.filter((option) => option.product === product.value.id)

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
  if (userInfo.fixed.includes(productId)) {
    userChange.value = '탈퇴하기'
  } else {
    userChange.value = '가입하기'
  }
})
</script>

<style scoped>
* {
 font-family: 'Orbit-Regular';
}
h1 {
  font-family: 'GamtanRoad Batang';
}
a {
  text-decoration: none;
  color: whitesmoke;
  font-size: 30px;
  width: 100%;
  height: 100%;
}
a:hover {
  color: #02040a;
}
.backbtn {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #83A2FF;
  color: whitesmoke;
}
.backbtn:active {
  background-color: rgb(133, 140, 188);
  box-shadow: inset 3px 3px 3px 3px  rgb(166, 175, 235);
  transition: 0.2s;
}

.join {
  width: 100%;
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

.out {
  width: 100%;
  height: 40px;
  border: 0px;
  border-radius: 40px;
  margin-top: 20px;
  background-color: rgb(214, 79, 101);
  font-family: 'KCC-Hanbit';
  font-size: 20px;
  color: whitesmoke;
}
.out:hover {
  background-color:rgb(230, 115, 134);
  transition: 0.5s;
}
.out:active {
  background-color: rgb(173, 62, 80);
  box-shadow: inset 3px 3px 3px 3px  rgb(129, 56, 69);
  transition: 0.2s;
}
</style>