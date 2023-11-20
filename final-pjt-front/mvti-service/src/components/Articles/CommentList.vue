<template>
    <div>
        <CommentCard
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"/>
    </div>
</template>

<script setup>
import CommentCard from './CommentCard.vue'

</script>

<style scoped>

</style>