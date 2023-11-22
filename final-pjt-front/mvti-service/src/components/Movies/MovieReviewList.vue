<template>
    <div class="card">
        <form @submit.prevent="reviewStore.createReview" class="d-flex">
            <div class="input-group">
                <input type="number" class="form-control" v-model.number="reviewStore.rating"
                    min="0" max="10" placeholder="평점 (0~10)">
                <input type="text" class="form-control" v-model.trim="reviewStore.content"
                    placeholder="한 줄 리뷰 남기기">
                <input type="submit" value="등록" class="btn btn-dark">
            </div>
        </form>
        <MovieReviewCard 
            v-for="review in filterReviews"
            :key="review.id"
            :review="review"/>
    </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import MovieReviewCard from './MovieReviewCard.vue'
import { useReviewStore } from '@/stores/review'

const reviewStore = useReviewStore()
const route = useRoute()

onMounted(() => {
    reviewStore.getReviews()
})

watch(() => route.params.id, () => {
    reviewStore.getReviews();
}, { immediate: true });

const filterReviews = computed(() => {
    const movieId = route.params.id
    return reviewStore.reviews.filter(review => review.movieId === movieId)
})
</script>

<style scoped>
.card {
    max-height: 250px;
    max-width: 750px;
    overflow: auto;
    padding: 10px;
    position: relative;
}

.input-group {
    display: flex;
    margin-bottom: 10px;
}

h6 {
    color: #f5f5f5;
}

.btn {
    white-space: nowrap;
}

</style>