<template>
    <div class="d-flex flex-column ms-4" @click="goDetail(movie)">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster">
        <h5 class="fw-bold">{{ movie.title }}</h5>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goDetail = function(movie) {
    router.push({ name:'detail', params: { id: `${movie.id}` } })
}

defineProps({
    movie: Object,
})
</script>

<style scoped>
img {
    width: 200px;
    height: 300px;
}

h5 {
    color: white;
    text-align: left;
    margin-top: 10px;
}
</style>