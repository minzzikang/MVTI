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
  <div>
    <RouterView />
  </div>
</template>

<style scoped>
div {
  background-color: rgb(20, 20, 20);
  height: 100vh;
  margin: 0;
}
</style>
