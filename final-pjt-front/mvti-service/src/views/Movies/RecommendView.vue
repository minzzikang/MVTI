<template>
    <div class="d-flex">
        <Navbar />
        <RecommendList class="ms-3"/>
    </div>
</template>

<script setup>
import RecommendList from '@/components/Movies/RecommendList.vue'
import Navbar from '@/components/Movies/Navbar.vue'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
    store.getMovies()
})

</script>

<style scoped>

</style>