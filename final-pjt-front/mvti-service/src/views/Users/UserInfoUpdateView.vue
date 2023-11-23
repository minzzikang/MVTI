<template>
    <div class="d-flex justify-content-center">
        <div class="d-flex w-100 justify-content-center align-items-center">
            <form @submit.prevent="updateUser" class="form-container w-50 bg-white p-4 border rounded">
                <h3>회원정보 수정</h3>
                <div class="mt-3">
                    <label for="nickname" class="form-label">닉네임:</label>
                    <input type="text" class="form-control mb-3" id="nickname" name="nickname" v-model.trim="nickname">

                    <label for="mbti" class="form-label">MBTI(대문자로 입력해 주세요!):</label>
                    <input type="text" class="form-control mb-3" id="mbti" name="mbti" v-model.trim="mbti">

                    <label for="age" class="form-label">나이:</label>
                    <input type="number" class="form-control mb-3" id="age" name="age" v-model.trim="age">

                    <div class="d-grid mt-3">
                        <input type="submit" class="btn btn-primary" value="수정 완료">
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'

const movieStore = useMovieStore()
const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

const nickname = ref('')
const mbti = ref('')
const age = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${movieStore.API_URL}/accounts/user`,
        headers: {
            Authorization: `Token ${movieStore.token}`
        }
    }).then(res => {
        console.log(res.data)
        const user = res.data
        nickname.value = user.nickname
        mbti.value = user.mbti
        age.value = user.age
    })
})

const updateUser = function () {
    axios({
        method: 'put',
        url: `${movieStore.API_URL}/accounts/userupdate/${userStore.user.pk}`,
        data: {
            nickname: nickname.value,
            mbti: mbti.value,
            age: age.value,
        },
        headers: {
            Authorization: `Token ${movieStore.token}`
        }
    }).then(res => {
        alert('회원 정보가 수정되었습니다.')
        router.push({ name: 'user'})
    }).catch(err => {
        console.log(err)
    })
}
</script>

<style  scoped>

</style>