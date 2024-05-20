<template>
  <div>
    <ul>
      <CommunityListItem 
      v-for="post in postList"
      :post = "post"
      @click-post-event="postDetail"
      />
    </ul>
  </div>
</template>

<script setup>
import CommunityListItem from '@/components/community/CommunityListItem.vue';
import {ref} from 'vue'
import { useRouter } from 'vue-router';

const postList = ref([
  {id: 1, title: 'sample1', content: 'sample1'},
  {id: 2, title: 'sample2', content: 'sample2'},
  {id: 3, title: 'sample3', content: 'sample3'},
  {id: 4, title: 'sample4', content: 'sample4'},
  {id: 5, title: 'sample5', content: 'sample5'},
])

const router = useRouter()
const postDetail = function (postId) {
  router.push({name:'postdetail', params: {'postId':postId}})
}
</script>

<style scoped>

</style>