<template>
    <div class="card mb-3 mt-3">
        <div class="card-body">
            <h5 class="card-title fw-bold">{{ article.title }}</h5>
            <p class="card-text">{{ article.content }}</p>
        </div>
    </div>
</template>

<script setup>
defineProps({
    article: Object
})
</script>

<style scoped>

</style>