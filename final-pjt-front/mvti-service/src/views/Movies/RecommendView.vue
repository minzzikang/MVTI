<template>
    <div class="d-flex">
        <Navbar />
        <div class="wrap-today">
            <RecommendTodayList class="ms-3" />
        </div>
    </div>
</template>

<script setup>
import RecommendTodayList from '@/components/Movies/RecommendTodayList.vue'
import Navbar from '@/components/Movies/Navbar.vue'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
    store.getMovies()
})

</script>

<style scoped>
.wrap-today {
    width: 100%;
    overflow: scroll;
    overflow: auto;
}
</style>