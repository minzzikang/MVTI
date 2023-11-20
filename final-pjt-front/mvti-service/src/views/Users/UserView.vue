<template>
    <div>
        <UserLikeList />
        <UserCommentMovieList />
        <UserArticleList />
        <UserCommentArticleList />
    </div>
</template>

<script setup>
import UserLikeList from '@/components/Users/UserLikeList.vue'
import UserCommentMovieList from '@/components/Users/UserCommentMovieList.vue'
import UserArticleList from '@/components/Users/UserArticleList.vue'
import UserCommentArticleList from '@/components/Users/UserCommentArticleList.vue'
</script>

<style scoped>

</style>