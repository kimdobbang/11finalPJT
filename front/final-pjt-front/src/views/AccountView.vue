<template>
  <div class="container d-flex justify-content-center align-items-center mt-4">
    <h1>계정</h1>
  </div>
  <hr class="border border-2 opacity-30">
  <div v-show="!signupClick">
    <AccountLoginForm />
    <RouterLink :to="{name: 'signup'}" @click="signupEvent">SignUp</RouterLink>
  </div>
  <RouterView />
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
.container {
  font-family:'GamtanRoad Batang';
  font-size: 25px;
}

</style>