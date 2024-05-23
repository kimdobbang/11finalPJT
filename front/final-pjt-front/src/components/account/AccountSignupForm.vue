<template>
  <div class="mb-5">
    <form @submit.prevent="signUpEvent">
      <img class="mb-4" src="@/assets/img/Logo.png" alt="" width="60" height="60">
      <h1 class="h3 mb-3 fw-normal">Pinyam 회원가입</h1>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="username" placeholder="아이디 입력" v-model="username">
        <label for="username">아이디</label>
      </div>

      <div class="form-floating my-3">
        <input type="password" class="form-control" id="password1" placeholder="비밀번호" v-model="password1">
        <label for="password1">비밀번호</label>
      </div>

      <div class="form-floating">
        <input type="password" class="form-control" id="password2" placeholder="비밀번호확인" v-model="password2">
        <label for="password2">비밀번호 확인</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="nikename" placeholder="닉네임 입력" v-model="nickname">
        <label for="nikename">닉네임</label>
      </div>

      <div class="mb-3">
        <label for="ile" class="form-label">프로필 사진</label>
        <input class="form-control" ref='inputImg' type="file" id="profile" name="profile" accept="image/*" @change="uploadImg">
      </div>

      <div class="form-floating my-3">
        <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="email">
        <label for="email">이메일 주소</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="age" placeholder="나이 입력" v-model="age">
        <label for="age">나이</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="money" placeholder="자산 입력" v-model="money">
        <label for="money">자산</label>
      </div>

      <div class="form-floating my-3">
        <input type="text" class="form-control" id="salary" placeholder="연 수입 입력" v-model="salary">
        <label for="salary">연 수입</label>
      </div>
        <div class="d-flex justify-content-center align-items-center">
        <input type="submit" value="회원가입" class="startbtn">
      </div>
    </form> 
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/accountstore';

const store = useAccountStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)
const email = ref(null)
const profileImg = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const inputImg = ref(null)

const uploadImg = function () {
  profileImg.value = inputImg.value.files[0]
}

const signUpEvent = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    email: email.value,
    profileImg: profileImg.value,
    age: age.value,
    money: money.value,
    salary: salary.value
  }
  store.signUp(payload)
}
</script>

<style scoped>
* {
  font-family: 'GamtanRoad Batang';
}
a {
  text-decoration: none;
}
.startbtn {
  width: 50%;
  height: 40px;
  border: 0px;
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