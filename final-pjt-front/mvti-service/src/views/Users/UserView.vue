<template>
    <div>
        <div style="color: white;">
            <p>userpage</p>
            <p>{{ user.username }}</p>
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

import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'

const store = useMovieStore()
const user = ref([])

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/user`,
        headers: {
        Authorization: `Token ${store.token}`
        }
    })
    .then((res) => {
        user.value = res.data
    })
    .catch((err) => console.log(err))
})

</script>

<style scoped>

</style>