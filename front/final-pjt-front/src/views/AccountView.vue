<template>
  <div class="container d-flex justify-content-center align-items-center mt-4">
    <h1>계정</h1>
  </div>
  <hr class="border border-2 opacity-30">
  <div class="d-flex flex-column justify-content-center align-items-center">
    <div v-show="!signupClick">
      <AccountLoginForm />
      <div class="ms-auto me-auto my-3 startbtn">
        <RouterLink :to="{name: 'signup'}" @click="signupEvent">회원가입</RouterLink>
      </div>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import AccountLoginForm from '@/components/account/AccountLoginForm.vue';
import { RouterLink } from 'vue-router';
import { ref } from 'vue';

const signupClick = ref(false)

const signupEvent = function () {
  signupClick.value = true
}
</script>
<style scoped>
a{
  text-decoration: none;
  color: rgb(125, 122, 122);
}
.container {
  font-family:'GamtanRoad Batang';
  font-size: 25px;
}
.startbtn {
  width: 50%;
  height: 40px;
  border: 0px;
  border-radius: 40px;
  background-color: #FFE3BB;
  font-family: 'KCC-Hanbit';
  font-size: 25px;
  color: whitesmoke;
  text-align: center;
}
.startbtn:hover {
  background-color: #FFD28F;
  transition: 0.5s;
}
.startbtn:active {
  background-color: #bf9c68;
  box-shadow: inset 3px 3px 3px 3px  #dcb57b;
  transition: 0.2s;
}
</style>