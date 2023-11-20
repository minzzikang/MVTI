<template>
    <div>
        <div>
            <p style="color: white;">userpage</p>
        </div>
        <UserLikeList />
        <UserCommentMovieList />
        <UserArticleList />
        <UserCommentArticleList />
    </div>
</template>

<script setup>
import UserLikeList from '@/components/Users/UserLikeList.vue'
import UserCommentMovieList from '@/components/Users/UserCommentMovieList.vue'
import UserArticleList from '@/components/Users/UserArticleList.vue'
import UserCommentArticleList from '@/components/Users/UserCommentArticleList.vue'

import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'

const store = useMovieStore()

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/user`,
        headers: {
        Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        console.log(res)
    })
    .catch((err) => console.log(err))
})

</script>

<style scoped>

</style>