<template>
    <div class="card">
        {{ article.title }}
        {{ article.content }}
    </div>
</template>

<script setup>
defineProps({
    article: Object
})
</script>

<style scoped>

</style>