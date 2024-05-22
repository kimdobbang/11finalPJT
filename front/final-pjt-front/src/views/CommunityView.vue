<template>
  <div>
    <h1>Community</h1>
  </div>  
  
  <RouterView />

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

</style>