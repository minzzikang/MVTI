import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])
  const API_URL = 'https://api.themoviedb.org/3/'
  const API_KEY = import.meta.env.VITE_TMDB_KEY

  const getMovies = function() {
    for (let i = 1; i < 10; i++) {
      axios({
        method: 'get',
        url: `${API_URL}/movie/popular?api_key=${API_KEY}&language=ko-KR&page=${i}`
      })
        .then((res) => {
          for (let j = 0; j < 20; j++) {
            console.log(res.data.results)
            // movies.value.push(res.data.results[j])
          }
        })
        .catch((err) => console.log(err))
    }
  }
  return { getMovies, movies }
}, { persist: true })
