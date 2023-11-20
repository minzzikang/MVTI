<template>
    <div>
        <form @submit.prevent="createComment">
            <label for="comment">댓글 내용: </label>
            <input type="text" id="comment" name="comment" v-model="content" placeholder="댓글을 입력하세요.">
            <input type="submit" value="등록">
        </form>
        <p v-for="comment in article.articlecomment_set"
            :key="comment.id"
            :comment="comment">
            {{ comment.id }} : {{ comment.content }}
        </p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const route = useRoute()
const store = useMovieStore()
const content = ref('')

defineProps({
    article: Object
})

const createComment = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/community/comment/`,
        data: {
            article: route.params.id,
            content: content.value
        },
        headers: {
            Authorization: `Token ${store.token}`
        },
    }).then(res => {
        article.value.articlecomment_set.push(res.data)
        content.value = ''
    }).catch(err => {
        console.log(err)
    })
}

</script>

<style scoped>

</style>