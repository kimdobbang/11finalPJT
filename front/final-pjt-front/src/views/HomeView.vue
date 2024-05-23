<template>
  <div class="position-absolute top-0 start-0" style="opacity: 0.7; width: 100%; height: 720px;">
  <img src="@/assets/img/backpie.gif" alt="backgroundgif" class="z-n1" style="width: 100%; height: 100%; object-fit: cover;">
  </div>
  <header class="d-flex justify-content-around align-items-center" style="height: 620px; background-color:rgba(0, 0, 0, 0.601)">
    <div class="z-2">
      <p class="text-center text-white">
        금융 정보를 맛있고 간편하게,<br><br>
        한 입에 냠냠<br><br>
        파이냠.
      </p>
    </div>
    <div class="z-2">
      <img src="@/assets/img/Logo.png" alt="Logo" style="width: 350px;">
    </div>
  </header>
  <content>
    <div class="d-flex" style="width: 100%; height: 720px;">
      <div class="d-flex justify-content-center align-items-center" style="width:50%; height: 100%;">
        <p class="text-center">
        모든 은행의<br><br>
        정기예금 / 적금 상품을<br><br>
        한 번에 비교!
        </p>
      </div>
      <div style="width:50%; height: 100%;">
        <img src="@/assets/img/1.png" alt="img1" style="width: 100w; height: 100%; object-fit: cover;">
      </div>
    </div>
    <div class="d-flex" style="width: 100%; height: 720px;">
      <div style="width:50%; height: 100%;">
        <img src="@/assets/img/2.png" alt="img2" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      <div class="d-flex justify-content-center align-items-center" style="width:50%; height: 100%;">
        <p class="text-center">
        주변 은행 찾기,<br><br>
        환율 확인과 계산까지<br><br>
        간편하게!
        </p>
      </div>
    </div>
    <div class="d-flex" style="width: 100%; height: 720px;">
      <div class="d-flex justify-content-center align-items-center" style="width:50%; height: 100%;">
        <p class="text-center">
        커뮤니티 게시판을 통해<br><br>
        자유로운 이야기와<br><br>
        유용한 정보도 공유!
        </p>
      </div>
      <div style="width:50%; height: 100%;">
        <img src="@/assets/img/3.png" alt="img3" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
    </div>
    <div class="d-flex flex-column justify-content-center align-items-center" style="width: 100%; height: 720px;">
      <div class="d-flex justify-content-center align-items-center" style="width:50%; height: 40%;">
        <p class="text-center">
        파이냠과 함께<br>
        알찬 금융생활을 시작하세요!
        </p>
      </div>
      <div @click="start" class="d-flex justify-content-center align-items-center startbtn">
        시작하기
      </div>
    </div>
  </content>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
const start = function () {
  router.push({name:'account'})
}
</script>

<style scoped>
@font-face {
    font-family: 'GamtanRoad Batang';
    font-weight: 400;
    font-style: normal;
    font-display: swap;
    src: url('https://cdn.jsdelivr.net/gh/fonts-archive/GamtanRoadBatang/GamtanRoadBatang-Regular.woff2') format('woff2'),
         url('https://cdn.jsdelivr.net/gh/fonts-archive/GamtanRoadBatang/GamtanRoadBatang-Regular.woff') format('woff'),
         url('https://cdn.jsdelivr.net/gh/fonts-archive/GamtanRoadBatang/GamtanRoadBatang-Regular.otf') format('opentype'),
         url('https://cdn.jsdelivr.net/gh/fonts-archive/GamtanRoadBatang/GamtanRoadBatang-Regular.ttf') format('truetype');

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
  font-family: 'GamtanRoad Batang';
  font-size: 35px;
}
.startbtn {
  width: 20%;
  height: 70px;
  border-radius: 40px;
  background-color: rgb(131, 162, 255);
  font-family: 'KCC-Hanbit';
  font-size: 25px;
  color: whitesmoke;
}
.startbtn:hover {
  background-color:rgb(180, 189, 255);
  transition: 0.5s;
}
.startbtn:active {
  background-color: rgb(133, 140, 188);
  box-shadow: inset 3px 3px 3px 3px  rgb(166, 175, 235);
  transition: 0.2s;
}
</style>