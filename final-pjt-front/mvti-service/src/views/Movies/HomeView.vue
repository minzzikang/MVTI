<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <div class="background d-flex">
        <div class="container d-flex justify-content-center align-items-center flex-column w-100">
        <div class="card w-25 p-2">
            <div class="card-body">
            <input class="form-control mb-2" type="text" placeholder="아이디를 입력하세요.">
            <input class="form-control mb-2" type="password" placeholder="비밀번호를 입력하세요.">
            <div class="d-flex justify-content-between">
                <RouterLink :to="{ name: 'signup'}">회원이 아니신가요?</RouterLink>
                <button class="btn btn-primary btn-sm">로그인</button>
            </div>
            </div>
        </div>
        </div>
    </div>
    
</template>

<style scoped>
.background {
  background-color: rgb(20, 20, 20);
  background-image: url('@/assets/background-img.png');
  height: 100vh;
  overflow: hidden;
  margin: 0;
  background-size: contain;
  background-position: center;
}
</style>