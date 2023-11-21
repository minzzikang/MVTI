<template>
    <div>
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster">
        <p>{{ movie.genres }}</p>
        <h5>{{ movie.title }}</h5>
        <!-- <p>{{ movie.overview }}</p> -->
    </div>
</template>

<script setup>
defineProps({
    movie: Object
})
</script>

<style scoped>

</style>