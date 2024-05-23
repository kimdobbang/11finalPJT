<template>
  <div class="container d-flex flex-column justify-content-center align-items-center mt-4">
    <h1>금융상품 목록</h1>
    <div>
      <ul class="nav nav-underline">
        <li class="nav-item">
          <RouterLink :to="{name: 'fixed'}" :class="[first ? 'nav-link active' : 'nav-link']" @click="nowArea(1)">정기예금</RouterLink> 
        </li>
        <li class="nav-item">
          <RouterLink :to="{name: 'installment'}" :class="[first ? 'nav-link' : 'nav-link active']" @click="nowArea(2)">적금</RouterLink>
        </li>
      </ul>
    </div>
  </div>
  <div class="d-flex justify-content-center align-items-center">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router';
import { onMounted,ref } from 'vue';

const router = useRouter()

const first = ref(true)

const nowArea = function (num) {
  if (num === 1) {
  first.value = true
} else {
  first.value = false
}}
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
.nav-link:hover {
  color: #83A2FF;
}
</style>