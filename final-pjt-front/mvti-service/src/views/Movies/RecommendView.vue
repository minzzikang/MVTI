<template>
    <div>
        <RouterLink :to="{ name: 'article' }">게시판</RouterLink>
        <RecommendList />
    </div>
</template>

<script setup>
import RecommendList from '@/components/Movies/RecommendList.vue'
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>