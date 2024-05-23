<template>
  <div class="container w-50 me-4 mt-3">
    <!-- 프로필 영역 -->
    <div class="top-area">
      <h3>금융전문가 냠냠봇GPT</h3>
      <p>안녕하세요 파이냠의 금융상품 추천 전문가 냠냠봇 GPT 입니다.</p>
    </div>
    <!-- 채팅 영역 -->
  <div class="card text-bg-dark">
    <div class="chat-area w-100">
      <h6 class="btn btn-success w-25">냠냠봇의 답변</h6>
      <!-- <p v-for="msg in chatContainer" :key="msg">{{ msg }}</p> -->
      <p @change="chatSave">
        {{ response }}
      </p>
    </div>
    <!-- 채팅창 하단 영역 -->
    <div class="bottom-area w-100">
      <form @submit.prevent="submitForm">
        <textarea
          class="chat-input w-100"
          id="prompt"
          v-model="prompt"
          placeholder="금융상품에 대해 도움이 필요하신가냠? 냠냠봇에 물어보세냠!"
        ></textarea>
        <button class="btn btn-primary" type="submit">질문하기</button>
      </form>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const prompt = ref('')
const response = ref('')
// const chatContainer = ref([])
// let oldMsg = ''

// const chatSave = function() {
//     chatContainer.value.push(response.value)
//     oldMsg =response.value
// }


const submitForm = async () => {
  try {
    const token = `${import.meta.env.VITE_OPENAI_API_KEY}`
    const res = await axios.post('http://127.0.0.1:8000/gpt/', 
      { prompt: prompt.value },
      {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      }
    );
    response.value = res.data.response
  } catch (error) {
    console.error('Error submitting the form:', error)
    response.value = '응답을 불러오는 중 오류가 발생했습니다.'
  }
};

</script>

<style scoped>
h3 {
  font-family: 'GamtanRoad Batang';
}
.profile-area {
  display: flex;
  align-items: center;
}

.chat-area {
  width: 100%;
  display: flex;
  flex: 1;
  background-color: var(--color-chat);
  padding: 10px;
  box-sizing: border-box;
  flex-direction: column;
  color: yellow;
}

/* 채팅 입력 iuput */
.chat-input {
  width: 100%;
  border: none;
  font-size: 16px;
  background-color: transparent;
  color: var(--color-text);
}

/* 입력창, 툴 */
.bottom-area {
  width: 100%;
  height: 13%;
  display: flex;
  padding: 10px 20px;
  box-sizing: border-box;
}

</style>
