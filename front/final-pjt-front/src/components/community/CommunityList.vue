<template>
  <div>
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

const communityStore = useCommunityStore()

onMounted(() => {
  communityStore.getArticles()
})
</script>

<style scoped>

</style>