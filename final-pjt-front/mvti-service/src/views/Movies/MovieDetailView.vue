<template>
    <div>
        <p style="color: white">{{ movieStore.movie }}</p>
        <DetailSimilarList />
    </div>
</template>

<script setup>
import DetailSimilarList from '@/components/Movies/DetailSimilarList.vue'
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const movieStore = useMovieStore()

onMounted(() => {
    movieStore.getMovieDetail()
})

</script>

<style scoped>

</style>
