import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useAccountStore } from '@/stores/accountstore'

export const useProductStore = defineStore('product', () => {
  // 기본 URL 지정
  const BASE_URL = 'http://127.0.0.1:8000'
  // 토큰 정보 가져오기
  const accountStore = useAccountStore()
  const TOKEN = accountStore.TOKEN
  // 상품 목록 변수 지정
  const fixed = ref([])
  const installment = ref([])

  // 예금 목록 받아오기
  const getFixed = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/products/fixed/`,
      headers: {
        Authorization: `Token ${TOKEN}`
      }
    })
    .then(res => {
      fixed.value = res.data
    })
    .catch(err => console.log(err))
  }
  // 적금 목록 받아오기
  const getInstallment = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/products/installment/`,
      headers: {
        Authorization: `Token ${TOKEN}`
      }
    })
    .then(res => {
      installment.value = res.data
    })
    .catch(err => console.log(err))
  }
  return { BASE_URL, TOKEN, getFixed, fixed, getInstallment, installment }
},{persist:true})
