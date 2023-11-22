<template>
    <h6>사용자 평점 및 리뷰</h6>
    <div class="card">
        <form @submit.prevent="reviewStore.createReview">
            <input type="number" class="form-control" v-model.number="reviewStore.rating"
                min="0" max="10" placeholder="평점을 입력하세요 (0~10)">
            <input type="text" class="form-control" v-model.trim="reviewStore.content" placeholder="리뷰를 남겨주세요.">
            <input type="submit" value="등록" class="btn btn-dark">
        </form>
        <MovieReviewCard 
            v-for="review in reviewStore.reviews"
            :key="review.id"
            :review="review"/>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import MovieReviewCard from './MovieReviewCard.vue'
import { useReviewStore } from '@/stores/review'

const reviewStore = useReviewStore()

onMounted(() => {
    reviewStore.getReviews()
})

</script>

<style scoped>
h6 {
    color: #f5f5f5;
}
</style>