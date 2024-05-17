import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useStore = defineStore('store', () => {
  // 기본 URL 지정
  const BASE_URL = 'http://127.0.0.1:8000'
  // 토큰 저장할 변수 지정
  const TOKEN = ref(null)

  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2, nickname, email, profileImg, age, money, salary } = payload
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/join/`,
      data: {
        username, password1, password2, nickname, email, profileImg, age, money, salary
      }
    })
    .then(res => {
      console.log('회원가입 성공')
      TOKEN = res.data.key
    })
    .catch(err => console.log(err))
  }
  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/login/`,
      data: {
        username,password
      },
      // headers: {
      //   Authorization: `Token ${TOKEN.value}`
      // }
    })
    .then(res => {
      console.log('로그인 성공')
      TOKEN = res.data.key
    })
    .catch(err => console.log(err))
  }

  return { BASE_URL, TOKEN, signUp, logIn }
},{persist:true})
