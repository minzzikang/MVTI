<template>
    <div>
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="poster">
        <p style="color: white;">{{ movie.title }}</p>
    </div>
</template>

<script setup>
defineProps({
    movie: Object
})
</script>

<style scoped>

</style>