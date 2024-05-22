<template>
  <div v-if="article">
    <h4>{{ articleId }}번 게시글</h4>
    <p>{{ article.title }}</p>
    <p>{{ article.user }}</p>
    <button v-if="accountStore.userNow.id === article.user" @click="updateEvent">update</button>
    <button v-if="accountStore.userNow.id === article.user" @click="deleteEvent">delete</button>
  </div>
</template>

<script setup>
import { useRoute,RouterLink } from 'vue-router';
import axios from 'axios';
import CommunityComment from '@/components/community/CommunityComment.vue';
import { useCommunityStore } from '@/stores/communitystore';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';
import router from '@/router';

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const route = useRoute()

const articleId = route.params.articleId
const article = ref(null)

const updateEvent = function () {
  console.log(article.value)
  router.push({name: 'articleupdate',query: {title: article.value.title, content: article.value.content, articleId: article.value.id}})
}

const deleteEvent = function () {
  axios({
    method: 'delete',
    url: `${communityStore.BASE_URL}/articles/${articleId}/`,
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(res => {
    console.log(res)
    console.log('삭제 성공')
    communityStore.getArticles();
    router.push({name: 'communitylist'})
  })
  .catch(err => console.log(err))
}
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
  })
  .catch(err => console.log(err))
})
</script>

<style scoped>

</style>