<template>
  <div>
    <!-- navbar -->
    <nav class="navbar">
      <RouterLink :to="{name: 'home'}">Home</RouterLink> |
      <RouterLink :to="{name: 'product'}">Product</RouterLink> |
      <RouterLink :to="{name: 'bank'}">Find Bank</RouterLink> |
      <RouterLink :to="{name: 'exchange'}">Exchange</RouterLink> |
      <RouterLink :to="{name: 'community'}">Community</RouterLink> |
      <RouterLink :to="{name: 'account'}" v-if="!accoutStore.TOKEN">Account</RouterLink>
      <RouterLink :to="{name: 'account'}" v-if="accoutStore.TOKEN" @click="logoutEvent">Logout</RouterLink>
    </nav>
    <RouterView />

  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router';
import { useAccountStore } from './stores/accountstore';
const accoutStore = useAccountStore()
const router = useRouter()
// 로그아웃 즉시 적용
const logoutEvent = function () {
  localStorage.removeItem('store')
  router.push({name:'home'})
}
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-around;
}
</style>