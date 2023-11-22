<template>
    <div class="container">
        <div class="d-flex flex-cloumn card">
            <div class="title-top">
                <h2>{{ store.article.title }}</h2>
                <font-awesome-icon :icon="['fas', 'circle-chevron-left']" size="2xl" class="back-icon" @click="goBack" />
            </div>
            <p>{{ store.article.username }}</p>
            <h5>{{ store.article.content }}</h5>
            <div class="d-flex justify-content-between align-items-center">
                <font-awesome-icon :icon="[isLike ? 'fas' : 'far', 'heart']"
                     @click="addLike(store.article.id)" />
                    {{ store.article.like_count }}
                    {{ store.article.is_like }}
                <div class="dates">
                    <p class="mb-0">작성일: {{ store.article.created_at }}</p>
                    <p>수정일: {{ store.article.updated_at }}</p>
                </div>
            </div>
            <CommentList :article="store.article" @new-comment="handleNewComment" @delete-comment="handleDeleteComment"
                @update-comment="handleUpdateComment" />
            <div class="d-flex align-items-center justify-content-end">
                <font-awesome-icon :icon="['fas', 'pen']" class="ms-2" @click="goEdit" />
                <font-awesome-icon :icon="['fas', 'trash-can']" class="ms-3"
                    @click="store.deleteArticle(store.article.id)" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import CommentList from '@/components/Articles/CommentList.vue'

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const movieStore = useMovieStore()

onMounted(() => {
    store.getArticleDetail()
})

const isLike = ref(false)

const addLike = function (articleId) {
    if (store.article.id === articleId) {
        isLike.value = !isLike.value
    }

    axios({
            method: 'post',
            url: `${store.API_URL}/community/article/${route.params.id}/likes`,
            data: {
                is_like: isLike.value
            },
            headers: {
                Authorization: `Token ${movieStore.token}`
            }
        })
            .then(res => {
                console.log(store.article)
                store.getArticleDetail()
            })
            .catch((err) => {
                console.error(err)
            })
}

const handleNewComment = (newComment) => {
    store.article.articlecomment_set.push(newComment)
}

const handleDeleteComment = (commentId) => {
    const index = store.article.articlecomment_set.findIndex((comment) => comment.id === commentId)
    store.article.articlecomment_set.splice(index, 1)
}

const handleUpdateComment = (updatedComment) => {
    const index = store.article.articlecomment_set.findIndex((comment) => comment.id === updatedComment.id)
    store.article.articlecomment_set[index] = updatedComment
}

const goBack = function () {
    router.push({ name: 'article' })
}

const goEdit = function () {
    router.push({ name: 'articleEdit' })
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