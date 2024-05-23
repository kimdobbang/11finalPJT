<template>
  <div>
    <h1>{{ user.username }} 님의 프로필 페이지</h1>
    <UserInfo />
    <UserProducts />
  </div>
</template>

<script setup>
import UserInfo from '@/components/profile/UserInfo.vue'
import UserProducts from '@/components/profile/UserProducts.vue'
import { useRoute,RouterLink } from 'vue-router';
import axios from 'axios';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';
import router from '@/router';

const accountStore = useAccountStore()
const route = useRoute()

const user = accountStore.userNow

</script>

<style scoped>

</style>