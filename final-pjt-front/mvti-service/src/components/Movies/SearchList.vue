<template>
    <div>
        <form @submit.prevent="searchMovie" class="form-control search-form">
            <input type="text" placeholder="검색어를 입력하세요"
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
    searchList.value.splice(0)
    if (inputText.value !== '' && inputText.value !== ' ' && inputText.value !== '  ') {
        for (let i = 0; i < store.movies.length; i++) {
            // 배우검색
            for (let j = 0; j < store.movies[i].actors.length; j++)
                if (store.movies[i].actors[j].name.toLowerCase().includes(inputText.value.toLowerCase())) {
                    if (searchList.value.some(movie => movie.id === store.movies[i].id)) {                        
                    } else {
                        searchList.value.push(store.movies[i])
                    }
                }
            // 제목검색
            if (store.movies[i].title.toLowerCase().includes(inputText.value.toLowerCase())) {
                if (searchList.value.some(movie => movie.id === store.movies[i].id)) {                        
                    } else {
                        searchList.value.push(store.movies[i])
                    }
            }
            // 감독 검색
            if (store.movies[i].director.name.toLowerCase().includes(inputText.value.toLowerCase())){
                if (searchList.value.some(movie => movie.id === store.movies[i].id)) {                        
                    } else {
                        searchList.value.push(store.movies[i])
                    }
            }
            // 내용 검색
            if (store.movies[i].overview.includes(inputText.value)) {
                if (searchList.value.some(movie => movie.id === store.movies[i].id)) {                        
                    } else {
                        searchList.value.push(store.movies[i])
                    }
            }
            // 장르 검색
            for (let j = 0; j < store.movies[i].genres.length; j++) {
                if (store.movies[i].genres[j].name === inputText.value) {
                    if (searchList.value.some(movie => movie.id === store.movies[i].id)) {                        
                    } else {
                        searchList.value.push(store.movies[i])
                    }
                }
            }
        }
    }
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