<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { onMounted } from 'vue'

const store = useMovieStore()

// onMounted(() => {
//   store.getMovies()
// })
</script>

<template>
  <div>
    <RouterLink :to="{ name: 'signup'}">회원가입</RouterLink>
  </div>
  <RouterView />
</template>

<style scoped>

</style>
