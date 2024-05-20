<template>
  <div>
    <form @submit.prevent="articleUpdate">
      <label for="title">title : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">content : </label>
      <textarea type="text" id="content" v-model.trim="content"></textarea><br>
      <input type="submit" value="update">
    </form>
  </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/communitystore';
import axios from 'axios';
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const communityStore = useCommunityStore()
const router = useRouter()
const route = useRoute()

const title = ref(route.query.title)
const content = ref(route.query.content)

const articleUpdate = function () {
  axios({
    method: 'put',
    url: `${communityStore.BASE_URL}/articles/${route.query.articleId}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(res => {
    router.push({name:'communitylist'})
  })
  .catch(err => console.log(err))
}
</script>

<style lang="scss" scoped>

</style>