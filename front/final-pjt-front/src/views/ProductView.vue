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
import { RouterLink, RouterView, useRouter } from 'vue-router';
import { onMounted } from 'vue';

const router = useRouter()

onMounted(() => {
  router.push({name:'fixed'})
})
</script>

<style scoped>

</style>