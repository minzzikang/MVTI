<template>
    <div>
        <Navbar />
        <div class="wrap-today">
            <RecommendTodayList class="ms-3" />
        </div>
        <div v-if="userStore.user.mbti">
            <RecommendMbtiList class="ms-3" />
        </div>
        <div v-else>
            <NoMbti class="ms-3" />
        </div>
    </div>
</template>

<script setup>
import RecommendTodayList from '@/components/Movies/RecommendTodayList.vue'
import RecommendMbtiList from '@/components/Movies/RecommendMbtiList.vue'
import NoMbti from '@/components/Movies/NoMbti.vue'
import Navbar from '@/components/Movies/Navbar.vue'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'

const movieStore = useMovieStore()
const userStore = useUserStore()

onMounted(() => {
    movieStore.getMovies()
    userStore.getUser()
})

</script>

<style scoped>
.wrap-today {
    width: 100%;
    overflow: scroll;
    overflow: auto;
}
</style>