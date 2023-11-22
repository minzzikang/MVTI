<template>
    <div class="ms-3">
        <span>{{ review.rating }}점</span>
        <span class="ms-3">{{ review.content }}</span>
        <div v-if="isEditing[review.id]" class="review-group">
            <input type="text" v-model="editingContent[review.id]" class="form-control" />
            <font-awesome-icon :icon="['fas', 'circle-check']" size='xl' class="ms-3"
                @click="saveEdit(review.id)"/>
            <font-awesome-icon :icon="['fas', 'circle-xmark']" size='xl' class="ms-2"
                @click="cancelEdit(review.id)"/>
        </div>
        <div v-else>
            <font-awesome-icon :icon="['fas', 'pen']" style="color: #aaaaaa;" class="ms-4" 
                @click="startEdit(review)"/>
            <font-awesome-icon :icon="['fas', 'trash-can']" style="color: #aaaaaa;" class="ms-3"
                @click="deleteComment(review.id)"/>
        </div>
        <hr>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useReviewStore } from '@/stores/review'
import { useMovieStore } from '@/stores/movie'

const reviewStore = useReviewStore()
const movieStore = useMovieStore()
const route = useRoute()

const content = ref('')
const rating = ref('')

const emit = defineEmits([])

const props = defineProps({
    review: Object
})

const movieId = route.params.id
const isEditing = ref([])
const editingReview = ref({})

const startEdit = (review) => {
    isEditing.value[review.id] = true
    editingReview.value[review.id] = review.content
}

const saveEdit = (reviewId) => {
    updateReveiw(reviewId, editingReview.value[reviewId])
    isEditing.value[reviewId] = false
}

const cancelEdit = (reviewId) => {
    isEditing.value[reviewId] = false
}

</script>

<style scoped>
.review-group {
    display: flex;
    align-items: center;
}
</style>