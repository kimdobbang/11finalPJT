<template>
  <div>
    <h2>기본 정보 수정</h2>
    <p>1</p>
    <button @click="updateEvent">update</button>
  </div>
</template>

<script setup>
import { useRoute,RouterLink } from 'vue-router';
import axios from 'axios';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';
import router from '@/router';

const accountStore = useAccountStore()
const route = useRoute()

const user = accountStore.userNow

const updateEvent = function () {
  console.log(article.value)
  router.push({name: 'articleupdate',query: {title: article.value.title, content: article.value.content, articleId: article.value.id}})
}

</script>

<style scoped>

</style>