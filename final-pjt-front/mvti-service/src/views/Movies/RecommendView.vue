<template>
    <div>
        <RouterLink :to="{ name: 'article' }">게시판</RouterLink>
        <RecommendList />
    </div>
</template>

<script setup>
import RecommendList from '@/components/Movies/RecommendList.vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
    store.getMovies()
})

</script>

<style scoped>

</style>