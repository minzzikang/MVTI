<template>
    <div class="d-flex justify-content-center">
        <div class="container d-flex flex-column">
            <h2 class="text-white mt-3">게시판</h2>
            <button class="btn btn-secondary btn-sm ms-auto">
            <RouterLink :to="{ name: 'create' }" class="link">새 글쓰기</RouterLink>
            </button>
            <ArticleList />
        </div>
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