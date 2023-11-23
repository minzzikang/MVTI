<template>
    <div class="card" @click="goDetail(movie)">
        {{ movie.title }}
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goDetail = function(movie) {
    router.push({ name:'detail', params: { id: `${movie.id}` } })
}

defineProps({
    movie: Object,
})

</script>

<style scoped>

</style>