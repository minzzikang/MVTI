<template>
    <div class="d-flex">
        <Navbar />
        <div class="ms-4 mt-3 d-flex flex-column" style="color: #f5f5f5;">
            <h3>{{ user.username }} 님의 프로필</h3>
            <font-awesome-icon :icon="['fas', 'key']" size="xl" style="color: #f5f5f5;"
                class="icon" @click="goUserUpdate"/>
            <font-awesome-icon :icon="['fas', 'arrow-right-from-bracket']" 
                size="xl" style="color: #f5f5f5;"
                @click="store.logOut"/>
        <UserLikeList />
        <UserCommentMovieList />
        <UserArticleList />
        <UserCommentArticleList />
        </div>
    </div>
</template>

<script setup>
import UserLikeList from '@/components/Users/UserLikeList.vue'
import UserCommentMovieList from '@/components/Users/UserCommentMovieList.vue'
import UserArticleList from '@/components/Users/UserArticleList.vue'
import UserCommentArticleList from '@/components/Users/UserCommentArticleList.vue'
import Navbar from '@/components/Movies/Navbar.vue'

import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
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

const goUserUpdate = function () {
    router.push({ name: 'userUpdate'})
}

</script>

<style scoped>
.icon {
    align-self: flex-start;
}
</style>