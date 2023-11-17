<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()
const userId = ref('')
const password = ref('')


</script>

<template>
    <div class="background d-flex">
        <div class="container d-flex justify-content-center align-items-center flex-column w-100">
        <div class="card w-25 p-2">
            <form @submit.prevent="logIn" class="card-body">
                <input class="form-control mb-2" type="text" placeholder="아이디를 입력하세요."
                    v-model.trim="userId">
                <input class="form-control mb-2" type="password" placeholder="비밀번호를 입력하세요."
                    v-model.trim="password">
                <div class="d-flex justify-content-between">
                    <RouterLink :to="{ name: 'signup'}">회원이 아니신가요?</RouterLink>
                    <input type="submit" value="로그인" class="btn btn-primary btn-sm">
                </div>
            </form>
        </div>
        </div>
    </div>
    
</template>

<style scoped>
.background {
  background-image: url('@/assets/background-img.png');
  overflow: hidden;
  background-size: contain;
  background-position: center;
}
</style>