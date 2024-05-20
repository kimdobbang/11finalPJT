import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('store', () => {
  // 기본 URL 지정
  const BASE_URL = 'http://127.0.0.1:8000'
  // 토큰 저장할 변수 지정
  const TOKEN = ref(null)
  // 라우터 변수 지정
  const router = useRouter()

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
      TOKEN.value = res.data.key
      router.push({name: 'home'})
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
    })
    .then(res => {
      console.log('로그인 성공')
      TOKEN.value = res.data.key
      router.push({name: 'home'})
    })
    .catch(err => console.log(err))
  }
  const isLogin = computed(() => {
    if (TOKEN.value === null) {
      return false
    } else {
      return true
    }
  })
  return { BASE_URL, TOKEN, signUp, logIn, isLogin }
},{persist:true})
