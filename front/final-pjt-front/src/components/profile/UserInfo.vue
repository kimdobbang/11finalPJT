<template>
  <div>
    <h3 class="text-center">기본 정보 수정</h3>
    <p>회원번호 {{ user.id }} </p>
    <p>ID {{ user.username }} </p>

    <form @submit.prevent="updateEvent()">
      <div class="form-floating my-3">
            <input type="text" class="form-control" id="nikename" placeholder="닉네임 입력" v-model="nickname">
            <label for="nikename">닉네임</label>
      </div>

      <div class="form-floating my-3">
        <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="email">
        <label for="email">이메일 주소</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="age" placeholder="나이 입력" v-model="age">
        <label for="age">나이</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="money" placeholder="자산 입력" v-model="money">
        <label for="money">자산</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="salary" placeholder="연 수입 입력" v-model="salary">
        <label for="salary">연 수입</label>
      </div>
        <div class="d-flex justify-content-center align-items-center">
        <input type="submit" value="수정하기" class="startbtn">
      </div>
    </form> 
    </div>


</template>


<script setup>
import { useRoute,RouterLink } from 'vue-router';
import axios from 'axios';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';
import router from '@/router';

const accountStore = useAccountStore()
const route = useRoute()

const user = accountStore.userNow
const email = ref(user.email)
const nickname = ref(user.nickname)
const age = ref(user.age)
const money = ref(user.money)
const salary = ref(user.salary)

const updateEvent = function () {
  axios({
    method: 'put',
    url: `${accountStore.BASE_URL}/accounts/getuser/${user.username}/`,
    data: {
      email: email.value,
      nickname: nickname.value,
      age: age.value,
      money: money.value,
      salary: salary.value
    },
    headers: {
      Authorization: `Token ${accountStore.TOKEN}`
    }
  })
  .then(res => {
    console.log('수정 완료!')
    alert('기본 정보가 수정되었습니다!')
    accountStore.userNow = res.data
  })
  .catch(err => {
    console.log(err)
    alert('입력 양식이 잘못 되었습니다. 올바른 양식으로 입력해주세요!')
  })
}
</script>

<style scoped>
* {
 font-family: 'Orbit-Regular';
}
h2 {
  font-family: 'GamtanRoad Batang';
}
.startbtn {
  width: 40%;
  height: 40px;
  border: 0px;
  border-radius: 40px;
  background-color: rgb(131, 162, 255);
  font-family: 'KCC-Hanbit';
  font-size: 18px;
  color: whitesmoke;
}
.startbtn:hover {
  background-color:rgb(180, 189, 255);
  transition: 0.5s;
}
.startbtn:active {
  background-color: rgb(133, 140, 188);
  box-shadow: inset 3px 3px 3px 3px  rgb(166, 175, 235);
  transition: 0.2s;
}
</style>