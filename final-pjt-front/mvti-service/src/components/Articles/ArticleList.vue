<template>
    <div>
        <div class="container p-2">
            <ArticleCard 
            v-for="article in store.articles" :key="article.id"
            :article="article"
            />
        </div>
    </div>
</template>

<script setup>
import ArticleCard from '@/components/Articles/ArticleCard.vue'
import axios from 'axios'
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()

onMounted(() => {
    store.getArticles()
})

</script>

<style scoped>
.container {
    background-color: white;
}
</style>