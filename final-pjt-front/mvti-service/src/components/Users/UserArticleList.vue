<template>
    <div>
        <p>좋아요한 게시글</p>
        <UserArticleCard
        v-for="article in userLikeArticle"
        :key="article.id"
        :article="article"/>
    </div>
</template>

<script setup>
import UserArticleCard from '@/components/Users/UserArticleCard.vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const articleStore = useArticleStore()
const userStore = useUserStore()

const userLikeArticle = computed(() => {
    return articleStore.articles.filter(article => {
        return article.article_like_users.includes(userStore.user.pk);
    })
})

</script>

<style scoped>

</style>