<template>
  <div>
    <h1>Account</h1>
  </div>
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

</style>