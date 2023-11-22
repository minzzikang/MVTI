<template>
    <div class="card">
        {{ movie.title }}
        <!-- {{ searchList.title }} -->
    </div>
</template>

<script setup>
defineProps({
    movie: Object,
    // searchList: Object
})
</script>

<style scoped>

</style>