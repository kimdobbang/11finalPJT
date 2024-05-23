<template>
  <div class="container d-flex flex-column justify-content-center align-items-center mt-4">
    <h1>금융상품 목록</h1>
    <div>
    <RouterLink :to="{name: 'fixed'}">정기예금</RouterLink> 
    <RouterLink :to="{name: 'installment'}">적금</RouterLink>
    </div>
    
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
a{
  text-decoration: none;
  color: rgb(125, 122, 122);
  margin-left: 20px;
  margin-right: 20px;
}
.container {
  font-family:'GamtanRoad Batang';
  font-size: 25px;
}
</style>