import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from './accountstore'
import axios from 'axios'


export const useExchangeStore = defineStore('exchange', () => {

  const API_URL = 'http://127.0.0.1:8000/exchanges/'
  const accountStore = useAccountStore()
  const TOKEN = accountStore.TOKEN

  // 1-1) 전체 환율 저장 변수
  const allexchangerates = ref([])

  // 1-2) 전체 환율정보 가져오기
  const getAllExchangeRates = function () {
    axios({
    method:'GET',
    url:`${API_URL}get-exchange/`,
    headers: {
      Authorization: `Token ${TOKEN}`
    }
  })
    .then(response => {
      console.log('결과'+response)
      console.log(response.data)
      allexchangerates.value = response.data
  })
    .catch(error => {
      console.log(error)
    })
} 

// =======================================================  

  // 2-1) 10개국 환율 저장 변수
  const exchangerates = ref([])
  
  // 2-2) 10개국 환율정보 가져오기
  const getExchangeRates = function () {
    axios({
    method:'GET',
    url:`${API_URL}get-exchange/`,
    headers: {
      Authorization: `Token ${TOKEN}`
    }
  })
    .then(response => {
      console.log('결과'+response)
      console.log(response.data)
      exchangerates.value = response.data
      exchangerates.value = exchangerates.value.filter((exchangerate) => {
        return exchangerate.CUR_UNIT === 'USD' || 
                exchangerate.CUR_UNIT === 'JPY' || 
                exchangerate.CUR_UNIT === 'EUR' || 
                exchangerate.CUR_UNIT === 'GBP' || 
                exchangerate.CUR_UNIT === 'CAD' || 
                exchangerate.CUR_UNIT === 'AUD' || 
                exchangerate.CUR_UNIT === 'CNH' || 
                exchangerate.CUR_UNIT === 'THB' || 
                exchangerate.CUR_UNIT === 'IDR' || 
                exchangerate.CUR_UNIT === 'HKD' 
        
      })
  })
    .catch(error => {
      console.log(error)
    })
} 

  return {API_URL,TOKEN, getExchangeRates, exchangerates, getAllExchangeRates, allexchangerates }
}, { persist: true})






