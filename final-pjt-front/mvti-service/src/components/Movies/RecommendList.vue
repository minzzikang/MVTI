<template>
    <div>
        <h3 class="text-white">오늘의 추천 영화</h3>
        <RecommendCard 
            v-for="movie in store.movies"
            :key="movie.id"
            :movie="movie"/>
    </div>
</template>

<script setup>
import RecommendCard from '@/components/Movies/RecommendCard.vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

</script>

<style scoped>

</style>