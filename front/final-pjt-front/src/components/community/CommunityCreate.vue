<template>
  <div>
    <form @submit.prevent="articleCreate">
      <label for="title">title :</label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">content :</label>
      <textarea id="content" v-model.trim="content"></textarea><br>
      <input type="submit" value="create">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCommunityStore } from '@/stores/communitystore';
import axios from 'axios';

const router = useRouter()
const communityStore = useCommunityStore()
const title = ref(null)
const content = ref(null)

const articleCreate = function () {
  axios({
    method: 'post',
    url: `${communityStore.BASE_URL}/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(() => {
    router.push({name: 'communitylist'})
  })
  .catch(err => console.log(err))
}
</script>

<style lang="scss" scoped>

</style>