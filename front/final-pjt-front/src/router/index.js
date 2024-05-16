import { createRouter, createWebHistory } from 'vue-router'
// view import
import HomeView from '@/views/HomeView.vue'
import AccountView from '@/views/AccountView.vue'
import ProductView from '@/views/ProductView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import BankView from '@/views/BankView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ProfileView from '@/views/ProfileView.vue'
import RecommendView from '@/views/RecommendView.vue'

// component import
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView,
      // children: [
      //   {path: 'login' , name: 'login', component: LoginForm},
      //   {path: 'signup' , name: 'signup', component: SignupForm},
      // ]
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/bank',
      name: 'bank',
      component: BankView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView
    },
    
  ]
})

export default router
