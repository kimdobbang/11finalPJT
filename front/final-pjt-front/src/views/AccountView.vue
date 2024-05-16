<template>
  <div>
    <h1>Account</h1>
    <RouterLink :to="{name: 'login'}">Login</RouterLink> |
    <RouterLink :to="{name: 'signup'}">SignUp</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>