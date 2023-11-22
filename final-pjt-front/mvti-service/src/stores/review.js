import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useMovieStore } from './movie'
import { useRoute } from 'vue-router'

export const useReviewStore = defineStore('review', () => {
	const reviews = ref([])
    const review = ref('')
	const API_URL = 'http://127.0.0.1:8000'
    const movieStore = useMovieStore()
    const route = useRoute()

	const getReviews = function () {
		axios({
			method: 'get',
			url: `${API_URL}/api/v1/movies/comment`,
			headers: {
				Authorization: `Token ${movieStore.token}`
			}
		}).then((res) => {
            // console.log(res.data)
			reviews.value = res.data
		}).catch((err) => {
			console.log(err)
		})
	}

    const content = ref('')
    const rating = ref(0)
    const movieId = ref(route.params.id)

    const createReview = function () {
  
        axios({
            method: 'post',
            url: `${API_URL}/api/v1/movies/${movieId.value}/comment`,
            data: {
                movie: route.params.id,
                content: content.value,
                rating: rating.value
            },
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        }).then(res => {
            getReviews()
            content.value = ''
        }).catch(err => {
            console.log(err)
        })
    }

	return { reviews, API_URL, getReviews, createReview,
        movieStore, content, review, movieId, rating
    }
}, { persist: true })
