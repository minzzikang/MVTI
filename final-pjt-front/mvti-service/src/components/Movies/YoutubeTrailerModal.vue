<template>
    <div>
        <font-awesome-icon :icon="['fab', 'youtube']" style="color: red;" size="2xl" class="video-icon" @click="isModalViewed(event)"/>
        <span class="ms-2 text-secondary">예고편 보기</span>

    <div class="modal-wrap" v-show="isModalView">
      <div class="modal-container">
        <iframe id="ytplayer" type="text/html" width="720" height="405"
        :src="`https://www.youtube.com/embed/${review.id.videoId}`"
        frameborder="0" allowfullscreen="allowfullscreen"></iframe>
        <button @click="isModalViewed(event)">닫기</button>
      </div>
    </div>

    </div>
</template>

<script setup>

</script>

<style scoped>

</style>