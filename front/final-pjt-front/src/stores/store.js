import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useStore = defineStore('store', () => {
  const BASE_URL = 'http://127.0.0.1:8000'
  const TOKEN = ref(null)
  // 회원가입
  const signUp = function () {

  }
  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/`,
      data: {
        username,password
      }
    })
    .then(res => {
      console.log('로그인 성공')
      TOKEN = res.data.key
    })
    .catch(err => console.log(err))
  }

  return { BASE_URL, TOKEN, signUp, logIn }
})
