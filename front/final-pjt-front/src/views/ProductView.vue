<template>
  <div>
    <h1>Product</h1>
    <RouterLink :to="{name: 'fixed'}">Fixed</RouterLink> |
    <RouterLink :to="{name: 'installment'}">Installment</RouterLink>
  </div>
  <div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>