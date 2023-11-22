<template>
    <div class="card">
        {{ movie.title }}
    </div>
</template>

<script setup>
defineProps({
    movie: Object
})
</script>

<style scoped>

</style>