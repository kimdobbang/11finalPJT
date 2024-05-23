<template>
  <div v-if="user" class="d-flex flex-column w-100 justify-content-center align-items-center">
    <div class="card border-dark w-100 d-flex flex-column">
      <div class="card-header w-100 d-flex flex-column">
        <h2 class="mb-0" style="align-self: center;">{{ article.title }} <span style="font-size: 15px;">작성자 : {{ user.username }}</span></h2>
      </div>  
      <div class="card-body" style="height: 30vh;">
        <p class="card-text">{{ article.content }}</p>
      </div>
      <div class="card-item d-flex justify-content-center mb-3">
        <button v-if="accountStore.userNow.id === article.user" @click="updateEvent" class="btn btn-outline-primary mx-2">수정</button>
        <button v-if="accountStore.userNow.id === article.user" @click="deleteEvent" class="btn btn-outline-danger mx-2">삭제</button>
      </div>
    </div>
    <hr class="border border-2 opacity-30">  
    <div class="d-flex form-floating my-3 w-100">
      <input type="text" class="form-control" id="floatingInput" placeholder="아이디 입력" v-model.trim="content">
      <label for="floatingInput">댓글 입력</label>
      <button class="ms-2 startbtn" @click="createComment">등록</button>
    </div>
    <ul class="list-group list-group-flush w-75 mb-4">
      <CommunityComment 
        v-for="comment in comments"
        :comment="comment"
        :key="comment.id"
        :getComments="getComments"
      />
    </ul>  
  </div>
</template>

<script setup>
import { useRoute,RouterLink,useRouter } from 'vue-router';
import axios from 'axios';
import CommunityComment from '@/components/community/CommunityComment.vue';
import { useCommunityStore } from '@/stores/communitystore';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const route = useRoute()
const router = useRouter()

const articleId = route.params.articleId
const article = ref(null)
const user = ref(null)

const content = ref('')
const comments = ref([])

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
    content.value = '';
    getComments();
    // 왜 아래 코드로 새로고침이 안되는걸까... 삭제화면도 마찬가지
    
  })
  .catch(err => console.log(err))
  } else {
    alert('댓글을 입력해주세요.')
  }
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
    getComments();
  })
  .catch(err => console.error(err));
});
</script>

<style scoped>
* {
  font-family: 'Orbit-Regular';
}
.startbtn {
  width: 20%;
  height: 55px;
  border: 0px;
  border-radius: 40px;
  background-color: rgb(131, 162, 255);
  font-family: 'KCC-Hanbit';
  font-size: 15px;
  color: whitesmoke;
}
.startbtn:hover {
  background-color:rgb(180, 189, 255);
  transition: 0.5s;
}
.startbtn:active {
  background-color: rgb(133, 140, 188);
  box-shadow: inset 3px 3px 3px 3px  rgb(166, 175, 235);
  transition: 0.2s;
}
</style>