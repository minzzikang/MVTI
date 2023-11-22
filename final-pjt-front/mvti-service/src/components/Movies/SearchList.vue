<template>
    <div>
        <form @submit.prevent="searchMovie" class="form-control search-form">
            <input type="text" placeholder="영화 제목을 검색해 보세요."
                v-model="inputText" class="input">
            <input type="submit" class="btn btn-primary btn-sm ms-2" value="찾기">
        </form>
        <SearchCard 
            v-for="movie in searchList"
            :key="movie.id"
            :movie="movie"/>
    </div>
</template>

<script setup>
import SearchCard from '@/components/Movies/SearchCard.vue'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios' 

const store = useMovieStore()
const inputText = ref('')
const searchList = ref([])

const searchMovie = function () {
    store.getMovies()
    // console.log(store.movies)
    searchList.value = store.movies.filter(movie => {
        // console.log(movie.title)
        // movie.title.includes(inputText.value)
        // console.log(inputText.value)
        movie.title === inputText.value
    })
    console.log(searchList.value)
}


</script>

<style scoped>
.search-form {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px 0;
}
.input {
    width: 50%;
}
</style>