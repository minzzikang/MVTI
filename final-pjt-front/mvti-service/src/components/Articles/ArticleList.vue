<template>
    <div>
        <div class="container p-2">
            <ArticleCard 
            v-for="article in articles" :key="article.id"
            :article="article"
            @add-like="handleAddLike"
            />
        </div>
    </div>
</template>

<script setup>
import ArticleCard from '@/components/Articles/ArticleCard.vue'
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const articles = ref([])

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then(res => {
        articles.value = res.data.map(article => ({
            ...article,
            isLike: false,
            likeCount: article.likeCount || 0
        }))
    })
    .catch(err => {
        console.log(err)
    })
})

const handleAddLike = function (articleId) {
    axios({
        method: 'post',
        url: `${store.API_URL}/community/article/${articleId}/likes`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then(res => {
        articles.value = articles.value.map(article => {
            if (article.id === articleId) {
                const updateIsLike = !article.isLike

                return {
                    ...article,
                    isLike: updateIsLike,
                    likeCount: updateIsLike ? (article.likeCount + 1) : (article.likeCount > 0 ? article.likeCount - 1 : 0)
                }
            }
            return article
        })
    }).catch(err => {
        console.log(err)
    })
}
</script>

<style scoped>
.container {
    background-color: white;
}
</style>