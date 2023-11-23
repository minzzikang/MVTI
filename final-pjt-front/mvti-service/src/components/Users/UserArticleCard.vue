<template>
    <div>
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