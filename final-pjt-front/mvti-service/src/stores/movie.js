import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
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
			url: `${API_URL}/api/v1/movies/`,
			headers: {
				Authorization: `Token ${token.value}`
			}
		}).then((res) => {
			movies.value = res.data
		}).catch((err) => {
			console.log(err)
		})
	}

	const route = useRoute()
	const movie = ref(null)
	const getMovieDetail = function () {
	  axios({
		method: 'get',
		url: `${API_URL}/api/v1/movies/${route.params.id}`,
		headers: {
		  Authorization: `Token ${token.value}`
	  }
	  })
		.then((res) => {
			movie.value = res.data
		})
		.catch((err) => {
			console.log(err)
		})
	  }

	const logIn = function (payload) {
		const { username, password } = payload

		axios({
			method: 'post',
			url: `${API_URL}/accounts/login/`,
			data: {
				username, password
			}
		}).then((res) => {
			// console.log(res.data)
			token.value = res.data.key
			router.push({ name: 'recommend' })
		}).catch((err) => {
			console.log(err)
		})
	}

	const logOut = function () {
		axios({
			method: 'post',
			url: `${API_URL}/accounts/logout/`,
		}).then(res => {
			alert('다음에 또 봐요~!')
			router.push({ name: 'home' })
		}).catch(err => {
			console.log(err)
		})
	}

	const signUp = function (payload) {
		const { username, password1, password2, nickname, mbti, age } = payload

		axios({
			method: 'post',
			url: `${API_URL}/accounts/signup/`,
			data: {
				username, password1, password2, nickname, mbti, age
			}
		}).then((res) => {
			const password = password1
			alert('회원이 되신 걸 환영합니다!')
			logIn({ username, password })
		}).catch((err) => {
			for (let i = 0; i < Object.values(err.response.data).length; i++) {
				for (let j = 0; j < Object.values(err.response.data)[i].length; j++) {
					alert(Object.values(err.response.data)[i][j])
				}
			}
			
		})
	}

	return { movies, token, API_URL, isLogin, getMovies, signUp, logIn, logOut, getMovieDetail, movie }
}, { persist: true })
