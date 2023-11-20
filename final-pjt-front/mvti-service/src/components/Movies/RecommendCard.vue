<template>
    <div>
        <img :src="movie.poster_path" alt="poster">
        <p>{{ movie.genre }}</p>
        <h5>{{ movie.title }}</h5>
        <p>{{ movie.overview }}</p>
    </div>
</template>

<script setup>
defineProps({
    movie: Object
})
</script>

<style scoped>

</style>