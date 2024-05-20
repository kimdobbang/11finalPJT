<template>
  <div>
    <h1>Community</h1>
  </div>  
  
  <RouterView />
  <!-- 게시글 상세는 아직 미구현 -->
</template>

<script setup>
import CommunityList from '@/components/community/CommunityList.vue';
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