<template>
    <div>
        <p>댓글 쓴 영화</p>
        <UserCommentMovieCard 
        v-for="movie in userCommentMovie"
        :key="movie.id"
        :movie="movie"/>
    </div>
</template>

<script setup>
import UserCommentMovieCard from '@/components/Users/UserCommentMovieCard.vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const movieStore = useMovieStore()
const userStore = useUserStore()

const userCommentMovie = computed(() => {
    return movieStore.movies.filter(movie => {
        return movie.moviecomment_set.some(comment => comment.id === userStore.user.pk);
    })
})


</script>

<style scoped>

</style>