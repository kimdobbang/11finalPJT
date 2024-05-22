import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useProductStore } from '@/stores/productstore'

export const useAccountStore = defineStore('account', () => {
  // 기본 URL 지정
  const BASE_URL = 'http://127.0.0.1:8000'
  // 토큰 저장할 변수 지정
  const TOKEN = ref(null)
  // 라우터 변수 지정
  const router = useRouter()
  // 현재 로그인 유저 정보 변수 지정
  const userNow = ref({})
  // 상품 목록 전달용 변수 지정
  const productStore = useProductStore()
  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload
    // 로그인 정보 유효성 검사용 데이터 보내기
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
      // 유저 정보를 가지고다니기 위해 유저정보 불러오기
      axios({
        method:'get',
        url: `${BASE_URL}/accounts/getuser/${username}/`,
        headers: {
          Authorization: `Token ${TOKEN.value}`
        }
      })
      .then(res => {
        userNow.value = res.data
        // 유저가 로그인할 때, 예금, 적금정보 db에 저장하기
        productStore.saveProduct()      
      })
      .catch(err => console.log(err))
      router.push({name: 'home'})
    })
    .catch(err => console.log(err))
  }
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
      console.log(res.data)
      TOKEN.value = res.data.key
      logIn({username: username, password: password2})
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
  return { BASE_URL, TOKEN, signUp, logIn, isLogin, userNow }
},{persist:true})
