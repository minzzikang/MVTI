<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { onMounted } from 'vue'

const store = useMovieStore()

onMounted(() => {
  store.getMovies()
})
</script>

<template>
  <RouterView />
</template>

<style scoped>

</style>
