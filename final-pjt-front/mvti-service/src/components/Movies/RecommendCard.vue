<template>
    <div class="d-flex flex-column ms-4">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster">
        <!-- <p>{{ movie.genres }}</p> -->
        <h5 class="fw-bold">{{ movie.title }}</h5>
    </div>
</template>

<script setup>
defineProps({
    movie: Object
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