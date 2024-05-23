<template>
  <div v-if="user">
    <h4>{{ articleId }}번 게시글</h4>
    <p>제목 : {{ article.title }}</p>
    <p>작성자 : {{ user.username }}</p>
    <button v-if="accountStore.userNow.id === article.user" @click="updateEvent">update</button>
    <button v-if="accountStore.userNow.id === article.user" @click="deleteEvent">delete</button>
    <input type="text" v-model="content"><button @click="createComment">댓글 입력</button>
    <CommunityComment 
      v-for="comment in comments"
      :comment="comment"
    />
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
const user = ref(null)

const content = ref('')
const comments = ref(null)

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

// 댓글 목록 받아오기
const getComments = function () {
    axios({
      method: 'get',
      url: `${communityStore.BASE_URL}/articles/${articleId}/comment/`,
      headers: {
        Authorization: `Token ${communityStore.TOKEN}`
      }
    })
    .then(res => {
      console.log(res)
      console.log('전체 댓글 조회 성공')
      comments.value = res.data
    })
    .catch(err => console.log(err))
    }

const createComment = function () {
  if (content.value !== '') {
  axios({
    method: 'post',
    url: `${communityStore.BASE_URL}/articles/${articleId}/comment/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(res => {
    console.log(res)
    console.log('댓글 입력 성공')
    // 왜 아래 코드로 새로고침이 안되는걸까... 삭제화면도 마찬가지
    // router.replace({ name: 'articledetail', params: { articleId: articleId } })
  })
  .catch(err => console.log(err))
  } else {
    alert('댓글을 입력해주세요.')
  }

  getComments()

}

// 작성자 정보 받아오기
const getuser = function () {
  console.log(communityStore.TOKEN)
  axios({
    method: 'get',
    url: `${communityStore.BASE_URL}/accounts/getuser2/${article.value.user}/`,
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(res => {
    if(res.data){
      console.log('작성자 정보 조회 완료');
      user.value = res.data
    }
  })
  .catch(err => console.log(err))
}

// 작성자 정보 안가져와져서 코드 수정함 (아래는 이전 코드)
// onMounted(() =>{
//   axios({
//     method:'get',
//     url: `${communityStore.BASE_URL}/articles/${articleId}/`,
//     headers: {
//       Authorization: `Token ${communityStore.TOKEN}`
//     }
//   })
//   .then(res => {
//     article.value = res.data
//   })
//   .catch(err => console.log(err))

//   getComments()
//   getuser()

// })

onMounted(() => {
  axios({
    method: 'get',
    url: `${communityStore.BASE_URL}/articles/${articleId}/`,
    headers: {
      Authorization: `Token ${communityStore.TOKEN}`
    }
  })
  .then(res => {
    article.value = res.data;
    return axios({
      method: 'get',
      url: `${communityStore.BASE_URL}/accounts/getuser2/${article.value.user}/`,
      headers: {
        Authorization: `Token ${communityStore.TOKEN}`
      }
    });
  })
  .then(res => {
    user.value = res.data;
    return axios({
      method: 'get',
      url: `${communityStore.BASE_URL}/articles/${articleId}/comment/`,
      headers: {
        Authorization: `Token ${communityStore.TOKEN}`
      }
    });
  })
  .then(res => {
    comments.value = res.data;
  })
  .catch(err => console.error(err));
});
</script>

<style scoped>

</style>