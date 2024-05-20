import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountStore } from '@/stores/accountstore'

export const useCommunityStore = defineStore('community', () => {
  // 기본 URL 지정
  const BASE_URL = 'http://127.0.0.1:8000'
  // 토큰 정보 가져오기
  const accountStore = useAccountStore()
  const TOKEN = accountStore.TOKEN
  // 게시글 목록 변수 지정
  const articles = ref([])


  // 게시글 목록 받아오기
  const getArticles = function () {
    console.log(TOKEN)
    axios({
      method: 'get',
      url: `${BASE_URL}/articles/`,
      headers: {
        Authorization: `Token ${TOKEN}`
      }
    })
    .then(res => {
      articles.value = res.data
    })
    .catch(err => console.log(err))
  }
  return { BASE_URL, TOKEN, getArticles, articles }
},{persist:true})
