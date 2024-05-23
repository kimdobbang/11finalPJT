<template>
 <div style="width: 100%;">
  <form @submit.prevent="logInEvent">
      <img class="mb-4" src="@/assets/img/Logo.png" alt="" width="60" height="60">
      <h1 class="h3 mb-3 fw-normal">Pinyam 로그인</h1>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="floatingInput" placeholder="아이디 입력" v-model.trim="username">
        <label for="floatingInput">아이디</label>
      </div>

      <div class="form-floating my-3">
        <input type="password" class="form-control" id="floatingPassword" placeholder="비밀번호" v-model.trim="password">
        <label for="floatingPassword">비밀번호</label>
      </div>
      <div class="d-flex justify-content-center align-items-center">
      <input type="submit" value="로그인" class="startbtn">
      </div>
    </form> 
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accountstore'

const store = useAccountStore()

const username = ref(null)
const password = ref(null)

const logInEvent = function () {
  const payload = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payload)
}
</script>

<style scoped>
* {
  font-family: 'GamtanRoad Batang';
}
a {
  text-decoration: none;
}
.startbtn {
  width: 50%;
  height: 40px;
  border: 0px;
  border-radius: 40px;
  background-color: rgb(131, 162, 255);
  font-family: 'KCC-Hanbit';
  font-size: 25px;
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