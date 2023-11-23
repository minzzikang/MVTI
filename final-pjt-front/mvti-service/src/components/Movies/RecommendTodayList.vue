<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">{{ season }}에 잘어울리는 영화!</h3>
        <div class="d-flex">
            <RecommendTodayCard 
                v-for="movie in movieList"
                :key="movie.id"
                :movie="movie"
            />
        </div>
    </div>
</template>

<script setup>
import RecommendTodayCard from '@/components/Movies/RecommendTodayCard.vue'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()
const movieList = ref([])

// 오늘 월 계산해서 계절별로 영화 추천
const today = new Date()
const month = today.getMonth() + 1
const season = ref('')
if (month >= 3 && month <= 5) {
    season.value = '봄'
} else if (month >= 6 && month <= 8) {
    season.value = '여름'
} else if (month >= 9 && month <= 11) {
    season.value = '가을'
} else {
    season.value = '겨울'
}

for (let i = 0; i < movieStore.movies.length; i++) {
    if (season.value === '봄') {
        if (movieStore.movies[i].overview.includes('재즈')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('사쿠라')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('따뜻한')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
                || movieStore.movies[i].title.includes('홀로')
                || movieStore.movies[i].title.includes('크리스마스')
                || movieStore.movies[i].title.includes('눈')
            ) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
    }
    if (season.value === '여름') {
        if (movieStore.movies[i].overview.includes('해변')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('여름')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
                || movieStore.movies[i].title.includes('해리')
                || movieStore.movies[i].title.includes('크리스마스')
                || movieStore.movies[i].title.includes('눈')
            ) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
    }
    if (season.value === '가을') {
        if (movieStore.movies[i].overview.includes('낭만')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
            movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('가을')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('만남')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
                || movieStore.movies[i].title.includes('포레')
                || movieStore.movies[i].title.includes('티파니')
                || movieStore.movies[i].title.includes('어벤')
            ) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
    }
    if (season.value === '겨울') {
        if (movieStore.movies[i].title.includes('겨울')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
            movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('크리스마스')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
        if (movieStore.movies[i].overview.includes('눈이')) {
            if (movieList.value.some(movie => movie.id === movieStore.movies[i].id)
                || movieStore.movies[i].title.includes('호빗')
                || movieStore.movies[i].title.includes('킹')
                || movieStore.movies[i].title.includes('존')
                || movieStore.movies[i].title.includes('로그')
            ) {                        
            } else {
                movieList.value.push(movieStore.movies[i])
            }
        }
    }
}

</script>

<style scoped>

</style>