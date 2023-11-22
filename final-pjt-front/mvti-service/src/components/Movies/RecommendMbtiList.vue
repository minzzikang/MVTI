<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">{{ userStore.user.mbti }}가 선호한 영화!</h3>
        <div class="d-flex">
            <RecommendMbtiCard
                v-for="movie in movieList"
                :key="movie.id"
                :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import RecommendMbtiCard from '@/components/Movies/RecommendMbtiCard.vue'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()
const userStore = useUserStore()
const movieList = ref([])

for (let i = 0; i < movieStore.movies.length; i++) {
    if (userStore.user.mbti === 'esfj'){
        if (movieStore.movies[i].overview.includes('배려')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('관심')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('감성')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
    }
}

</script>

<style scoped>

</style>