<template>
    <div>
        <h3 class="text-white">새 글쓰기</h3>
        <form @submit.prevent="createArticle">
            <label for="title" class="form-label">제목:</label>
            <input type="text" class="form-control" id="title" name="title" v-model.trim="title">

            <label for="content" class="form-label">내용:</label>
            <textarea class="form-control" id="content" name="content" rows="5" v-model.trim="content"></textarea>
            <div class="d-grid">
                <input type="submit" class="btn btn-primary" value="작성 완료">
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()

const title = ref('')
const content = ref('')

const createArticle = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/community/article/`,
        data: {
            title: title.value,
            content: content.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then(res => {
        router.push({ name: 'article'})
    }).catch(err => {
        console.log(err)
    })
}
</script>

<style scoped>
label {
    color: white;
}
</style>