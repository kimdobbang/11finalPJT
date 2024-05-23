<template>
  <h1 class="mt-3 text-center">{{ user.username }} 님의 프로필 페이지</h1>
  <div class="container d-flex flex-wrap justify-content-around mt-4">
    <div class="col-5">
      <UserInfo />
    </div>
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
h1 {
  font-family: 'GamtanRoad Batang';
}
</style>