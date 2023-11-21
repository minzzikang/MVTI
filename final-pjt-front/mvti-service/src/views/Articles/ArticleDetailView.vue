<template>
    <div class="container">
        <div class="d-flex flex-cloumn card">
            <div class="title-top">
                <h2>{{ article.title }}</h2>
                <font-awesome-icon :icon="['fas', 'circle-chevron-left']" size="2xl" class="back-icon"
                    @click="goBack"/>
            </div>
            <p>{{ article.username }}</p>
            <h5>{{ article.content }}</h5>
            <div class="dates">
                <p class="mb-0">작성일: {{ article.created_at }}</p>
                <p>수정일: {{ article.updated_at }}</p>
            </div>
            <CommentList :article="article"
                @new-comment="handleNewComment"
                @delete-comment="handleDeleteComment"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import CommentList from '@/components/Articles/CommentList.vue'

const route = useRoute()
const router = useRouter()
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

const handleDeleteComment = (commentId) => {
    const index = article.value.articlecomment_set.findIndex((comment) => comment.id === commentId)
    article.value.articlecomment_set.splice(index, 1)
}

const goBack = function () {
    router.push({ name: 'article'})
}

</script>

<style scoped>
.container {
    max-width: 700px;
    padding: 20px;
    margin: auto;
}
.card {
    background-color: #f9f9f9;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 20px;
}
.card h3 {
    color: #333;
    font-size: 24px;
}
.title-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.dates {
    align-self: flex-end;
    text-align: right;
    font-size: 0.8rem;
    color: #666;
}

</style>