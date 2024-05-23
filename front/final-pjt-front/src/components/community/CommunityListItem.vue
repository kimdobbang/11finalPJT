<template>
  <tr>
    <td>{{ article.id }}</td>
    <td><RouterLink
    :to="{name:'articledetail', params:{articleId:article.id} }">
    {{ article.title }}</RouterLink></td>
    <td><RouterLink
    :to="{name:'articledetail', params:{articleId:article.id} }">
    {{ article.content }}</RouterLink></td>
    
  </tr>
</template>

<script setup>
import {ref} from 'vue'
import { RouterLink } from 'vue-router';
defineProps({
  article: Object
})


</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}
a:hover {
  color: #83A2FF;
  transition: 0.4s;
}
</style>