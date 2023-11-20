<template>
    <div>
        <h2 class="text-white">게시판</h2>
        <button class="btn btn-secondary">
        <RouterLink :to="{ name: 'create' }" class="link">새 글쓰기</RouterLink>
        </button>
        <ArticleList />
    </div>
</template>

<script setup>
import ArticleList from '@/components/Articles/ArticleList.vue'
import { RouterLink } from 'vue-router'

</script>

<style scoped>
.link {
    text-decoration: none;
    color: white;
}
</style>