<template>
    <div class="d-flex p-4">
        <img :src="`https://image.tmdb.org/t/p/w300/${store.movie.poster_path}`" alt="poster">
        <div class="d-flex flex-column ms-3">
            <h3>{{ store.movie.title }}</h3>
            <p>{{ store.movie.overview }}</p>
            <h6>감독 : {{ store.movie.director }}</h6>
            <h6>출연진 : {{ store.movie }}</h6>
        </div>
        <DetailSimilarList />
    </div>
</template>

<script setup>
import DetailSimilarList from '@/components/Movies/DetailSimilarList.vue'
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
    store.getMovieDetail()
})

</script>

<style scoped>
img {
    width: 300px;
    height: 500px;
}
h3, p, h6 {
    color: #f5f5f5;
}
</style>