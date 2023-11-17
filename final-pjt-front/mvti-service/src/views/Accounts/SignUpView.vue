<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form class="form-container w-50 bg-white p-4 border rounded">
                <h4>회원 가입을 환영합니다!</h4>
                <div class="mt-3">
                    <label for="userId">아이디</label>
                    <input type="text" name="userId" id="userId" class="form-control mb-3">
                    <label for="PW">비밀번호</label>
                    <input type="password" name="PW" id="PW" class="form-control mb-3" placeholder="영문, 숫자, 특문 중 2개 조합 8자 이상">
                    <label for="pwCheck">비밀번호 확인</label>
                    <input type="password" name="pwCheck" id="pwCheck" class="form-control mb-3">
                    <label for="nickname">닉네임</label>
                    <input type="text" name="nickname" id="nickname" class="form-control mb-3" placeholder="2자 이상">
                    <label for="age">나이</label>
                    <input type="text" name="age" id="age" class="form-control mb-3">
                    <label for="mbti">본인의 MBTI는? (선택사항)</label>
                    <input type="text" name="mbti" id="mbti" class="form-control mb-3">
                    <input type="submit" class="btn btn-primary mt-3" value="가입하기">
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()
const userId = ref('')
const password = ref('')
const passwordCheck = ref('')
const nickname = ref('')
const mbti = ref('')


</script>

<style scoped>

</style>