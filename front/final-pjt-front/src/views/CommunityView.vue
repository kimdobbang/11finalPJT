<template>
  <div class="container d-flex flex-column justify-content-center align-items-center mt-4">
    <h1>금융생활 꿀팁 공유 게시판</h1>
  </div>
  <hr class="border border-2 opacity-30">  
  <div class="container d-flex flex-column align-items-center">
    <RouterView />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCommunityStore } from '@/stores/communitystore';
import { useRouter,RouterView } from 'vue-router';

const communityStore = useCommunityStore()
const router = useRouter()

onMounted(() => {
  router.push({name:'communitylist'})
})
</script>

<style scoped>
h1 {
  font-family: 'GamtanRoad Batang';
}
</style>