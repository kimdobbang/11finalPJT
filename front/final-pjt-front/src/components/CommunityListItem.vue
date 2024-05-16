<template>
  <li>
    <h4 @click="postClick">{{ post.title }} - {{ post.content }}</h4>
  </li>
</template>

<script setup>
import {ref} from 'vue'
const props = defineProps({
  post: Object
})

const emit = defineEmits(['clickPostEvent'])
const postId = ref(props.post.id)
const postClick = function () {
  emit('clickPostEvent', postId.value)
}

</script>

<style scoped>

</style>