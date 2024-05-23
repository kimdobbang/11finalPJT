<template>
  <div>
    <h2>기본 정보 수정</h2>
    <p>회원번호 {{ user.id }} </p>
    <p>ID {{ user.username }} </p>
    <p>
      <label>Email</label>
      <input v-model="email" type="text" />
    </p>
    <p>
      <label>Nickname</label>
      <input v-model="nickname" type="text" />
    </p>
    <p>
      <label>나이</label>
      <input v-model="age" type="text" />
    </p>
    <p>
      <label>현재 가진 금액</label>
      <input v-model="money" type="text" />
    </p>
    <p>
      <label>연봉</label>
      <input v-model="salary" type="text" />
    </p>
    <button @click="updateEvent()">수정하기</button>
  </div>
</template>

<script setup>
import { useRoute,RouterLink } from 'vue-router';
import axios from 'axios';
import { useAccountStore } from '@/stores/accountstore';
import { onMounted, ref } from 'vue';
import router from '@/router';

const accountStore = useAccountStore()
const route = useRoute()

const user = accountStore.userNow
const email = ref(user.email)
const nickname = ref(user.nickname)
const age = ref(user.age)
const money = ref(user.money)
const salary = ref(user.salary)

const updateEvent = function () {
  axios({
    method: 'put',
    url: `${accountStore.BASE_URL}/accounts/getuser/${user.username}/`,
    data: {
      email: email.value,
      nickname: nickname.value,
      age: age.value,
      money: money.value,
      salary: salary.value
    },
    headers: {
      Authorization: `Token ${accountStore.TOKEN}`
    }
  })
  .then(res => {
    console.log('수정 완료!')
    alert('기본 정보가 수정되었습니다!')
    accountStore.userNow = res.data
  })
  .catch(err => {
    console.log(err)
    alert('입력 양식이 잘못 되었습니다. 올바른 양식으로 입력해주세요!')
  })
}
</script>

<style scoped>

</style>