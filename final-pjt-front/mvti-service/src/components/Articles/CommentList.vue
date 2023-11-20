<template>
    <div>
        <form @submit.prevent="createComment" class="comment-form mb-3">
            <div class="input-group">
                <input type="text" id="comment" name="comment" v-model="content" placeholder="댓글을 입력하세요." class="form-control">
                <input type="submit" value="등록" class="btn btn-dark">
            </div>
        </form>
        <p v-for="comment in article.articlecomment_set"
            :key="comment.id"
            :comment="comment">
            {{ comment.id }} : {{ comment.content }}
            <hr>
        </p>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const route = useRoute()
const store = useMovieStore()
const content = ref('')
const emit = defineEmits(['newComment'])

const props = defineProps({
    article: Object
})

const articleId = ref(route.params.id)

const createComment = function () {
    axios({
        method: 'post',
        url: `${store.API_URL}/community/article/${articleId.value}/comment`,
        data: {
            article: route.params.id,
            content: content.value
        },
        headers: {
            Authorization: `Token ${store.token}`
        },
    }).then(res => {
        emit('newComment', res.data)
        content.value = ''
    }).catch(err => {
        console.log(err)
    })
}

</script>

<style scoped>
.comment-form {
    display: flex;
    flex-direction: column;   
}

.input-group {
    display: flex;
}
</style>