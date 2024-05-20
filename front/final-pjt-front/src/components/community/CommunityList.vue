<template>
  <div>
    <RouterLink :to="{name: 'articlecreate'}">[CREATE]</RouterLink>
    <ul>
      <CommunityListItem 
      v-for="article in communityStore.articles"
      :article = "article"
      />
    </ul>
  </div>
</template>

<script setup>
import CommunityListItem from '@/components/community/CommunityListItem.vue'
import {onMounted, ref} from 'vue'
import { useCommunityStore } from '@/stores/communitystore'
import { RouterLink } from 'vue-router';
const communityStore = useCommunityStore()

onMounted(() => {
  communityStore.getArticles()
})
</script>

<style scoped>

</style>