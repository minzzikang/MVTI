<template>
    <div>
        <span>{{ review.rating }}</span>
        <span>{{ review.content }}</span>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useReviewStore } from '@/stores/review'
import { useMovieStore } from '@/stores/movie'

const reviewStore = useReviewStore()

const props = defineProps({
    review: Object
})

</script>

<style scoped>

</style>