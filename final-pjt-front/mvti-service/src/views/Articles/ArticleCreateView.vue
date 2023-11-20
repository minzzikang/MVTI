<template>
    <div>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/api/v1/`
    })
}
</script>

<style scoped>

</style>