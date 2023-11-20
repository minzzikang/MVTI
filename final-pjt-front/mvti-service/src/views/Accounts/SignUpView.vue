<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="signUp" class="form-container w-50 bg-white p-4 border rounded">
                <h4>회원 가입을 환영합니다!</h4>
                <div class="mt-3">
                    <label for="username">아이디</label>
                    <input type="text" name="username" id="username" class="form-control mb-3" v-model.trim="username">
                    <label for="PW">비밀번호</label>
                    <input type="password" name="PW" id="PW" class="form-control mb-3" 
                        placeholder="영문, 숫자, 특문 중 2개 조합 8자 이상" v-model.trim="password1">
                    <label for="pwCheck">비밀번호 확인</label>
                    <input type="password" name="pwCheck" id="pwCheck" class="form-control mb-3" v-model.trim="password2">
                    
                    <p v-if="!passwordMatch" class="text-danger">
                        비밀번호가 일치하지 않습니다.
                    </p>

                    <label for="nickname">닉네임</label>
                    <input type="text" name="nickname" id="nickname" class="form-control mb-3"
                        placeholder="2자 이상" v-model.trim="nickname">
                    
                    <label for="age">나이</label>
                    <input type="number" name="age" id="age" class="form-control mb-3" v-model.trim="age">
                    
                    <div v-if="!allFilled" class="alert alert-danger">
                        필수 사항 정보를 채워주세요.
                    </div>

                    <label for="mbti">본인의 MBTI는? (선택사항)</label>
                    <input type="text" name="mbti" id="mbti" class="form-control mb-3" v-model.trim="mbti">
                    <input type="submit" class="btn btn-primary mt-3" value="가입하기">
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const nickname = ref('')
const age = ref('')
const mbti = ref('')

const passwordMatch = ref(true)
const allFilled = ref(true)

const signUp = function () {
    // allFilled.value = username.value && password.value && passwordCheck.value && nickname.value && age.value

    // if (!allFilled.value) {
    //     return
    // }

    // if (password.value !== passwordCheck.value) {
    //     passwordMatch.value = false
    //     return
    // }

    const payload = {
        username: username.value,
        password1: password1.value,
        password2: password2.value,
        nickname: nickname.value,
        mbti: mbti.value,
        age: age.value,
    }
    store.signUp(payload)
}

// watch([password, passwordCheck], () => {
//     passwordMatch.value = password.value === passwordCheck.value
// })

</script>

<style scoped>

</style>