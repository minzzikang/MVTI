<template>
    <div class="container">
        <div class="card">
            <p>작성일: {{ article.created_at }}</p>
            <p>수정일: {{ article.updated_at }}</p>
            <p>작성자: {{ article.username }}</p>
            <hr>
            <h3>{{ article.title }}</h3>
            <p>{{ article.content }}</p>
            <hr>
            <CommentList :article="article" @new-comment="handleNewComment"/>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import CommentList from '@/components/Articles/CommentList.vue'

const route = useRoute()
const store = useMovieStore()

const article = ref('')
const articleId = ref(route.params.id)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/${articleId.value}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.error(err)
    })
})

const handleNewComment = (newComment) => {
    article.value.articlecomment_set.push(newComment)
}

</script>

<style scoped>

</style>