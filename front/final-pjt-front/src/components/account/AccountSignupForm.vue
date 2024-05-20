<template>
  <div>
    <h1>SignUp</h1>
  </div>
  <form @submit.prevent="signUpEvent">
    <label for="username">username : </label>
    <input type="text" id="username" v-model="username"><br>

    <label for="password1">password : </label>
    <input type="password" id="password1" v-model="password1"><br>

    <label for="password2">password confirm: </label>
    <input type="password" id="password2" v-model="password2"><br>

    <label for="nickname">nickname : </label>
    <input type="text" id="nickname" v-model="nickname"><br>

    <label for="email">email : </label>
    <input type="email" id="email" v-model="email"><br>

    <!-- <div>
      <img ref="showImg" v-show="profileImg">
    </div> -->
    <label for="profile">profile img :</label>
    <input ref='inputImg' type="file" id="profile" name="profile" accept="image/*" @change="uploadImg">
    <br>

    <label for="age">age: </label>
    <input type="text" id="age" v-model="age"><br>

    <label for="money">money : </label>
    <input type="text" id="money" v-model="money"><br>

    <label for="salary">salary : </label>
    <input type="text" id="salary" v-model="salary"><br>


    <input type="submit" value="signup">
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from '@/stores/accountstore';

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
  console.log(profileImg.value)
  store.signUp(payload)
}
</script>

<style scoped>

</style>