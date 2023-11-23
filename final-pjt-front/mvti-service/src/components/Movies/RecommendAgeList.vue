<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">당신의 친구들이 좋아하는 영화!</h3>
        <div class="d-flex">
            <RecommendAgeCard
                v-for="movie in movieList"
                :key="movie.id"
                :movie="movie"/>
        </div>
    </div>
</template>

<script setup>
import RecommendAgeCard from '@/components/Movies/RecommendAgeCard.vue'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()
const userStore = useUserStore()
const movieList = ref([])

for (let i = 0; i < movieStore.movies.length; i++) {
    if (userStore.user.age < 20) {
        for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
            if (movieStore.movies[i].genres[j].name === '애니메이션') {
                if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
                } else {
                    movieList.value.push(movieStore.movies[i])
                }
            }
        }
    }
    if (userStore.user.age >= 20 && userStore.user.age < 30) {
        for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
            if (movieStore.movies[i].genres[j].name === '액션') {
                if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
                } else {
                    movieList.value.push(movieStore.movies[i])
                }
            }
        }
    }
    if (userStore.user.age >= 30 && userStore.user.age < 40) {
        for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
            if (movieStore.movies[i].genres[j].name === '로맨스') {
                if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
                } else {
                    movieList.value.push(movieStore.movies[i])
                }
            }
        }
    }
    if (userStore.user.age >= 40 && userStore.user.age < 50) {
        for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
            if (movieStore.movies[i].genres[j].name === '미스터리') {
                if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
                } else {
                    movieList.value.push(movieStore.movies[i])
                }
            }
        }
    }
    if (userStore.user.age >= 50) {
        for (let j = 0; j < movieStore.movies[i].genres.length; j++) {
            if (movieStore.movies[i].genres[j].name === '역사') {
                if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {
                } else {
                    movieList.value.push(movieStore.movies[i])
                }
            }
        }
    }
}
</script>

<style scoped>

</style>