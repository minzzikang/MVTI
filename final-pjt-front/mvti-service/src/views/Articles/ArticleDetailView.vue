<template>
    <div>
        <img src="" alt="poster">
        <p>{{ article.title }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'

const route = useRoute()
const store = useMovieStore()

const article = ref('')
const articleId = route.params.id

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/${articleId}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.error(err)
    })
})

</script>

<style scoped>

</style>