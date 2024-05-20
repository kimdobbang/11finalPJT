<template>
  <div>
    <h1>Login</h1>
  </div>
  <form @submit.prevent="logInEvent">
    <label for="username">username : </label>
    <input type="text" id="username" v-model.trim="username"><br>
    <label for="password">password : </label>
    <input type="password" id="password" v-model.trim="password"><br>
    <input type="submit" value="login">
  </form>
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

</style>