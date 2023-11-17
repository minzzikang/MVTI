import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const router = useRouter()
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  
  const token = ref(null)
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      movies.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const signUp = function (payload) {
    const { userId, password, passwordCheck } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        userId, password, passwordCheck
      }
    }).then((res) => {
      console.log(res)
      alert('회원이 되신 걸 환영합니다!')
    }).catch((err) => {
      console.log(err)
    })
  }

  const logIn = function (payload) {
    const { userId, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        userId, password
      }
    }).then((res) => {
      console.log(res.data)
      token.value = res.data.key
    }).catch((err) => {
      console.log(err)
    })
  }
  return { movies, API_URL }
})
