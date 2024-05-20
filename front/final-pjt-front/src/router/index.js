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
import AccountLoginForm from '@/components/account/AccountLoginForm.vue'
import AccountSignupForm from '@/components/account/AccountSignupForm.vue'
import ProductFixedList from '@/components/product/ProductFixedList.vue'
import ProductInstallmentList from '@/components/product/ProductInstallmentList.vue'
import CommunityList from '@/components/community/CommunityList.vue'
import CommunityListItemDetail from '@/components/community/CommunityListItemDetail.vue'

// store import
import { useAccountStore } from '@/stores/accountstore'


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
      children: [
        {path: 'login' , name: 'login', component: AccountLoginForm},
        {path: 'signup' , name: 'signup', component: AccountSignupForm},
      ]
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView,
      children: [
        {path: 'fixed' , name: 'fixed', component: ProductFixedList},
        {path: 'installment' , name: 'installment', component: ProductInstallmentList},
      ]
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
      component: CommunityView,
      children: [
        {path: '' , name: 'communitylist', component: CommunityList},
        {path: ':articleId' , name: 'articledetail', component: CommunityListItemDetail},
      ]
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
router.beforeEach((to,from) =>{
  const accountStore = useAccountStore()
  if (to.name != 'home' && to.name != 'account' && to.name !='login' && to.name != 'signup' && !accountStore.isLogin) {
    alert('Please Login')
    return {name: 'account'}
  } else if (to.name === 'account' && accountStore.isLogin) {
    alert('Already Login')
    return {name: 'home'}
  }
})
export default router
