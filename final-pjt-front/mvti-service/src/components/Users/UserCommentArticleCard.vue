<template>
    <div class="card">
        <p>{{ article.title }}</p>
    </div>
</template>

<script setup>
defineProps({
    article: Object
})
</script>

<style scoped>

</style>