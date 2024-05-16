<template>
  <div>
    <h4>{{ route.params.key }}번 게시글</h4>
    <p>블라블라</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute()
</script>

<style scoped>

</style>