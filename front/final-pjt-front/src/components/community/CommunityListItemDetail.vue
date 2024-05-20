<template>
  <div v-if="article">
    <h4>{{ articleId }}번 게시글</h4>
    <p>{{ article.title }}</p>
    <p>{{ article.user }}</p>
    <button v-if="accountStore.userNow.id === article.user">[update]</button>
    <button v-if="accountStore.userNow.id === article.user">[delete]</button>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useCommunityStore } from '@/stores/communitystore';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const route = useRoute()


const articleId = route.params.articleId
const article = ref(null)

onMounted(() =>{
  axios({
    method:'get',
    url: `${communityStore.BASE_URL}/articles/${articleId}/`,
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(res => {
    article.value = res.data
    console.log(article.value)
  })
  .catch(err => console.log(err))
})
</script>

<style scoped>

</style>