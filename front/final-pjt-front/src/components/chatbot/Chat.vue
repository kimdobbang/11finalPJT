<!-- <template>
  <div> -->
    <!-- 프로필 영역 -->
        <!-- <h3>금융 전문가 냠냠봇 GPT</h3>
      <p>안녕하세요! 냠냠봇이 금융상품 추천 해드려요!</p> -->
    <!-- 채팅 영역 -->
      <!-- <div v-for="(message, index) in messages" :key="index" :class="[message.role + '-chat', 'chat']">
        {{ message.content }}
      </div> -->
    <!-- 채팅창 하단 영역 -->
      <!-- <input class="chat-input" type="text" placeholder="금융상품 추천을 요청해보세요" v-model="userInput" @keyup.enter="chatSubmit" />
      </div>
</template>

<script setup>
import OpenAI from 'openai'
import { ref } from 'vue';
import axios from 'axios';

const messages = ref([]);
const userInput = ref('');
const OPEN_API_URL = 'https://api.openai.com/v1/chat/completions';
const API_KEY = `${import.meta.env.VITE_OPENAI_API_KEY}`;

const openai = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'],
})
sync function main() {
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: 'Say this is a test' }],
    model: 'gpt-3.5-turbo',
  })
}

main()

</script> -->
<!-- 
<style lang="scss" scoped>
</style> -->
<template>
  <div>

  </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>