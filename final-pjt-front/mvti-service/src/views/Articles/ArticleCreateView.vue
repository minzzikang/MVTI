<template>
    <div>
        <h3 class="text-white">새 글쓰기</h3>
        <form @submit.prevent="store.createArticle">
            <label for="title" class="form-label">제목:</label>
            <input type="text" class="form-control" id="title" name="title" v-model.trim="store.title">

            <label for="content" class="form-label">내용:</label>
            <textarea class="form-control" id="content" name="content" rows="5" v-model.trim="store.content"></textarea>
            <div class="d-grid">
                <input type="submit" class="btn btn-primary" value="작성 완료">
            </div>
        </form>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'

const store = useArticleStore()

</script>

<style scoped>
label {
    color: white;
}
</style>