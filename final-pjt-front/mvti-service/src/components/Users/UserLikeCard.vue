<template>
    <div>
        <p style="color: white;">{{ movie.title }}</p>
    </div>
</template>

<script setup>
defineProps({
    movie: Object
})
</script>

<style scoped>

</style>