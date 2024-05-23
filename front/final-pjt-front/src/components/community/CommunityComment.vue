<template>
  <li v-if="user" class="list-group-item">
    <p v-show="comment.user !== userNow.id">
      {{ comment.content }} - {{ user.username }}
    </p>
    <div v-show="comment.user == userNow.id">
      <input type="text" v-model="content" style="border: none;">
      <div class="card-item d-flex justify-content-end">
        <button v-if="accountStore.userNow.id === comment.user" @click="updateComment" class="btn btn-outline-primary mx-2">수정</button>
        <button v-if="accountStore.userNow.id === comment.user" @click="deleteComment" class="btn btn-outline-danger mx-2">삭제</button>
      </div>
    </div>
  </li>
</template>

<script setup>
  import { onMounted, ref } from 'vue';
  import { useRouter,RouterLink } from 'vue-router';
  import axios from 'axios';
  import { useCommunityStore } from '@/stores/communitystore';
  import { useAccountStore } from '@/stores/accountstore';
  
  const router = useRouter()
  const communityStore = useCommunityStore()
  const accountStore = useAccountStore()
  const props = defineProps({
  comment: Object,
  getComments: Function
})

  const user = ref(null)
  const userNow = accountStore.userNow

  const content = ref(props.comment.content)

  // 작성자 정보 받아오기
  const getuser = function () {
      console.log(communityStore.TOKEN)
      axios({
        method: 'get',
        url: `${communityStore.BASE_URL}/accounts/getuser2/${props.comment.user}/`,
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

  // 댓글 삭제하기
  const deleteComment = function () {
      console.log(communityStore.TOKEN)
      axios({
        method: 'delete',
        url: `${communityStore.BASE_URL}/articles/${props.comment.article}/comment/${props.comment.id}/`,
        headers: {
          Authorization: `Token ${communityStore.TOKEN}`
        }
      })
      .then(res => {
          console.log('댓글 삭제 완료')
          // 왜 아래 코드로 새로고침이 안되는걸까 22
          props.getComments()
      })
      .catch(err => console.log(err))
    }

  // 댓글 수정하기
  const updateComment = function () {
      console.log(communityStore.TOKEN)
      axios({
        method: 'put',
        url: `${communityStore.BASE_URL}/articles/${props.comment.article}/comment/${props.comment.id}/`,
        data: {
          content: content.value
        },
        headers: {
          Authorization: `Token ${communityStore.TOKEN}`
        }
      })
      .then(res => {
          console.log('댓글 수정 완료')
          // 왜 아래 코드로 새로고침이 안되는걸까 333
          props.getComments()

      })
      .catch(err => console.log(err))
    }

  onMounted(() => {

    getuser()

    })
</script>

<style scoped>

</style>