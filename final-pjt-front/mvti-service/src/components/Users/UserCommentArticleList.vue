<template>
    <div>
        <p>댓글 쓴 게시글</p>
        <UserCommentArticleCard 
        v-for="article in userCommentArticle"
        :key="article.id"
        :article="article"/>
    </div>
</template>

<script setup>
import UserCommentArticleCard from '@/components/Users/UserCommentArticleCard.vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const articleStore = useArticleStore()
const userStore = useUserStore()

const userCommentArticle = computed(() => {
    return articleStore.articles.filter(article => {
        return article.articlecomment_set.some(comment => comment.id === userStore.user.pk);
    })
})

// console.log(articleStore.articles)
</script>

<style scoped>

</style>