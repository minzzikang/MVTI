<template>
    <div class="container">
        <h3 class="text-white mb-3 mt-3">오늘의 추천 영화</h3>
        <div class="d-flex">
            <RecommendCard 
                v-for="movie in store.movies"
                :key="movie.id"
                :movie="movie"
            />
        </div>
    </div>
</template>

<script setup>
import RecommendCard from '@/components/Movies/RecommendCard.vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

</script>

<style scoped>

</style>