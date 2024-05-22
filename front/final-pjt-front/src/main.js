import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'


import { useKakao } from 'vue3-kakao-maps/@utils'
useKakao(`${import.meta.env.VITE_KAKAO_API_KEY}`, ['clusterer', 'services', 'drawing']); // 각 라이브러리는 ',(콤마)'로 구분합니다.
const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
app.mount('#app')
