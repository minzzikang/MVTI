<template>
    <div class="card">
        <p style="color: white;">{{ article.title }}</p>
    </div>
</template>

<script setup>
defineProps({
    article: Object
})
</script>

<style scoped>

</style>