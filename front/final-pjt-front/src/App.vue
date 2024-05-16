<template>
  <div>
    <!-- navbar -->
    <nav class="navbar">
      <RouterLink :to="{name: 'product'}">Product</RouterLink> |
      <RouterLink :to="{name: 'bank'}">Find Bank</RouterLink> |
      <RouterLink :to="{name: 'exchange'}">Exchange</RouterLink> |
      <RouterLink :to="{name: 'community'}">Community</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-around;
}
</style>