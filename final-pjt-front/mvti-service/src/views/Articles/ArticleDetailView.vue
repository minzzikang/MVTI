<template>
    <div class="container">
        <div class="card">
            <h3>{{ article.title }}</h3>
            <p>{{ article.content }}</p>
        </div>
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
const articleId = ref(route.params.id)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/${articleId.value}`,
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