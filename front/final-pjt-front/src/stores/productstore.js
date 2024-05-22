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
  const fixedList = ref([])
  const fixedOptions = ref([])
  const installmentList = ref([])
  const installmentOptions = ref([])


  // 로그인 시 정보 요청하여 저장
  const saveProduct = function () {
    // 이거 TOKEN은 할당이 안됨;;;;;;; community는 똑같이써도 할당 되는데. 
    // 순서가 이상한가 봤더니, 순서는 안이상하고 오히려 community가 더 위에있는데도 잘됨.
    // 그 다음 then 으로 들어가는건데, 안됨
    // accountStore.TOKEN이라고 하면 잘 뽑힘
    console.log(accountStore.TOKEN)
    axios({
      method: 'get',
      url: `${BASE_URL}/products/save-fixed/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      console.log('Fixed Save Complete!')
    })
    .catch(err => console.log(err))

    axios({
      method: 'get',
      url: `${BASE_URL}/products/save-installment/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      console.log('Installment Save Complete!')
      alert('로그인 시 진행한 예/적금 불러오기가 완료되었습니다!')  
    })
    .catch(err => {
      console.log(err)
      alert('로그인 시 진행한 예/적금 불러오기에 오류가 발생되었습니다. 로그아웃 후 다시 로그인해주세요')  
      
  })
  }

  // 예금 목록 받아오기
  const getFixed = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/products/get-fixed/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      fixedList.value = res.data
     //예금 옵션 받아오기
     axios({
      method: 'get',
      url: `${BASE_URL}/products/get-fixedOption/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
     })
     .then(res => {
      fixedOptions.value = res.data
     })
     .catch(err => console.log(err))
    })
    .catch(err => console.log(err))
  }
  // 적금 목록 받아오기
  const getInstallment = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/products/get-installment/`,
      headers: {
        Authorization: `Token ${accountStore.TOKEN}`
      }
    })
    .then(res => {
      installmentList.value = res.data
      //적금 옵션 받아오기
      axios({
       method: 'get',
       url: `${BASE_URL}/products/get-installmentOption/`,
       headers: {
         Authorization: `Token ${accountStore.TOKEN}`
       }
      })
      .then(res => {
       installmentOptions.value = res.data
      })
      .catch(err => console.log(err))
     })
     .catch(err => console.log(err))
    }
  return { BASE_URL, TOKEN, saveProduct, fixedList, fixedOptions, getFixed, 
    installmentList, installmentOptions, getInstallment }
},{persist:true})
