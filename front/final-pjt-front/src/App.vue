<template>
    <!-- navbar -->
    <nav class="navbar navbar-expand-xl border-bottom border-body d-flex justify-content-around p-3 " data-bs-theme="dark" style="background-color: rgba(0, 0, 0, 0.792); z-index: 99;">
      <div>
        <button class="navbar-toggler justify-content-around" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <RouterLink :to="{name: 'home'}">
          <img src="@/assets/img/Logo.png" alt="Logo" style="width: 70px;">
        </RouterLink>
      </div>
      <div class="collapse navbar-collapse " id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink :to="{name: 'product'}">예/적금 목록</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{name: 'bank'}">주변 은행 찾기</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{name: 'exchange'}">환율</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{name: 'communitylist'}">커뮤니티</RouterLink>
          </li>
        </ul>
      </div>
      <div>
        <RouterLink :to="{name: 'profile'}" v-if="accoutStore.isLogin">My Profile</RouterLink>
        <RouterLink :to="{name: 'account'}" v-if="!accoutStore.isLogin" class="login">로그인 / 회원가입</RouterLink>
        <RouterLink :to="{name: 'login'}" v-if="accoutStore.isLogin" @click="logoutEvent">Logout</RouterLink>
      </div>
    </nav>

    <RouterView />

    <footer class="position-absolute end-0 d-flex justify-content-center align-items-center" style="background-color: rgba(0, 0, 0, 0.792); width: 100%; height: 100px;">
      <div class="me-4">
        <img src="@/assets/img/Logo.png" alt="Logo" style="width: 50px;">
      </div>
      <div>
        <p class="m-0">
          2024 Finyam.<br>
          Team.KimJeongJoe
        </p>
      </div>
    </footer>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router';
import { useAccountStore } from './stores/accountstore';
const accoutStore = useAccountStore()
const router = useRouter()
// 로그아웃 즉시 적용
const logoutEvent = function () {
  localStorage.removeItem('account')
  router.go()
}
</script>

<style scoped>
@font-face {
    font-family: 'KCC-Hanbit';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2403-2@1.0/KCC-Hanbit.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
a {
  text-decoration: none;
  font-size: 25px;
  font-family: 'KCC-Hanbit';
  color: whitesmoke;
  margin-left: 40px;
  margin-right: 40px;
}
p {
  text-decoration: none;
  font-size: 15px;
  font-family: 'KCC-Hanbit';
  color: whitesmoke;
  margin-left: 40px;
  margin-right: 40px;
}
.login {
  font-size: 15px;
}
</style>