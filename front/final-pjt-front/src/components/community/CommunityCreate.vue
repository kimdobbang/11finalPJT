<template>
  <div class="w-50">
    <h3 class="text-center">새 글 작성</h3>
    <form @submit.prevent="articleCreate">
      <div class="form-floating my-3">
        <input type="text" class="form-control" id="title" placeholder="제목 입력" v-model.trim="title">
        <label for="title">제목</label>
      </div>

      <div class="form-floating my-3">
        <textarea class="form-control" id="content" placeholder="내용 입력" v-model.trim="content" style="height: 150px"></textarea>
        <label for="content">내용</label>
      </div>


      <div class="d-flex justify-content-center align-items-center">
        <input type="submit" value="게시" class="out">
      </div>
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

<style scoped>
* {
  font-family: 'Orbit-Regular';
}
.out {
  width: 40%;
  height: 40px;
  border: 0px;
  border-radius: 40px;
  margin-top: 20px;
  background-color: rgb(214, 79, 101);
  font-family: 'KCC-Hanbit';
  font-size: 20px;
  color: whitesmoke;
}
.out:hover {
  background-color:rgb(230, 115, 134);
  transition: 0.5s;
}
.out:active {
  background-color: rgb(173, 62, 80);
  box-shadow: inset 3px 3px 3px 3px  rgb(129, 56, 69);
  transition: 0.2s;
}
</style>