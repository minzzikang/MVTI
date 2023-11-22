<template>
    <div>
        <h3 class="text-white mb-3 mt-3">{{ userStore.user.mbti }}가 선호한 영화!</h3>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

</script>

<style lang="scss" scoped>

</style>