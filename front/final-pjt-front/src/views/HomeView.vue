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
        <img src="@/assets/img/01.jpg" alt="img1" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
    </div>
    <div class="d-flex" style="width: 100%; height: 720px;">
      <div style="width:50%; height: 100%;">
        <img src="@/assets/img/02.jpg" alt="img2" style="width: 100%; height: 100%; object-fit: cover;">
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
        <img src="@/assets/img/03.jpg" alt="img3" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
    </div>
    
    

    <div>

    </div>
  </content>
</template>

<script setup>

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
p {
  font-family: 'GamtanRoad Batang';
  font-size: 35px;
}

</style>