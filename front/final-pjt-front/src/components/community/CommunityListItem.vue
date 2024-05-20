<template>
  <li>
    <RouterLink
    :to="{name:'articledetail', params:{articleId:article.id} }">
    {{ article.title }} - {{ article.content }}</RouterLink>
  </li>
</template>

<script setup>
import {ref} from 'vue'
import { RouterLink } from 'vue-router';
defineProps({
  article: Object
})


</script>

<style scoped>

</style>