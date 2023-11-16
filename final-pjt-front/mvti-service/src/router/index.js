import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/Movies/HomeView.vue'
import SignUpView from '@/views/Accounts/SignUpView.vue'
import RecommendView from '@/views/Movies/RecommendView.vue'
import SearchView from '@/views/Movies/SearchView.vue'
import MovieDetailView from '@/views/Movies/MovieDetailView.vue'
import ArticleCreateView from '@/views/Articles/ArticleCreateView.vue'
import ArticleView from '@/views/Articles/ArticleView.vue'
import ArticleDetailView from '@/views/Articles/ArticleDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/mvti',
      name: 'recommend',
      component: RecommendView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: MovieDetailView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/article/:id',
      name: 'articleDetail',
      component: ArticleDetailView
    },
  ]
})

export default router
