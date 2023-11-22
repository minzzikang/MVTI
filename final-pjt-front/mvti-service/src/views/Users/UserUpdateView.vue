<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="userUpdate" class="form-container w-50 bg-white p-4 border rounded">
                <h3>비밀번호 변경</h3>
                <div class="mt-3">
                    <label for="password">새로운 비밀번호</label>
                    <input type="password" name="password" id="password" class="form-control mb-3"
                        placeholder="영문, 숫자, 특문 중 2개 조합 8자 이상" v-model.trim="new_password1">
                    <label for="pwCheck">비밀번호 확인</label>
                    <input type="password" name="pwCheck" id="pwCheck" class="form-control mb-3" v-model.trim="new_password2">

                    <p v-if="!passwordMatch" class="text-danger">
                        비밀번호가 일치하지 않습니다.
                    </p>
                    <input type="submit" class="btn btn-primary mt-3" value="수정">
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import axios from 'axios'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()

const new_password1 = ref('')
const new_password2 = ref('')
const passwordMatch = ref(true)

const userUpdate = function () {
    if (new_password1.value !== new_password2.value) {
        passwordMatch.value = false
        return
    }
    passwordMatch.value = true

    axios({
        method: 'post',
        url: `${store.API_URL}/accounts/password/change/`,
        data: {
            new_password1: new_password1.value,
            new_password2: new_password2.value,
        },
        headers: {
            Authorization: `Token ${store.token}`
        }
    }).then(res => {
        alert('비밀번호가 변경되었습니다. 다시 로그인해주세요.')
        router.push({ name: 'home' })
    }).catch(err => {
        console.log(err)
    })
}
</script>

<style scoped></style>