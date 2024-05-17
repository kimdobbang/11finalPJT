<template>
  <div>
    <h1>Login</h1>
  </div>
  <form @submit.prevent="logInEvent">
    <label for="username">username : </label>
    <input type="text" id="username"><br>
    <label for="password">password : </label>
    <input type="password" id="password"><br>
    <input type="submit" value="login">
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from '@/stores/store';

const store = useStore()

const username = ref(null)
const password = ref(null)

const logInEvent = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>

</style>