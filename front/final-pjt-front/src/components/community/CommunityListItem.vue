<template>
  <li>
    <RouterLink :to="`/community/${articleId}`">{{ article.title }} - {{ article.content }}</RouterLink>
  </li>
</template>

<script setup>
import {ref} from 'vue'
import { RouterLink } from 'vue-router';
const props = defineProps({
  article: Object
})
const articleId = ref(props.article.id)

</script>

<style scoped>

</style>