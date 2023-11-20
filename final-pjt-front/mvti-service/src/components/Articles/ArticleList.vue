<template>
    <div>
        <div class="container p-2">
            <ArticleCard 
            v-for="article in articles" :key="article.id"
            :article="article"/>
        </div>
    </div>
</template>

<script setup>
import ArticleCard from '@/components/Articles/ArticleCard.vue'
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const articles = ref([])

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/community/article/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then(res => {
        articles.value = res.data
    })
    .catch(err => {
        console.log(err)
    })
})

</script>

<style scoped>
.container {
    background-color: white;
}
</style>