<template>
    <div>
      <div @click="isModalViewed(event)">
        <font-awesome-icon :icon="['fab', 'youtube']"
        style="color: red;"
        size="2xl" 
        class="video-icon"/>
        <span class="ms-2 text-secondary">예고편 보기</span>
      </div>

      <div class="modal-wrap" v-show="isModalView">
        <div class="modal-container">
          <p>{{ movie.trailer_key }}</p>
          <iframe
          :key="youtubeTrailer"
          id="ytplayer"
          type="text/html"
          width="720"
          height="405"
          :src="`https://www.youtube.com/embed/${youtubeTrailer}`"
          frameborder="0" allowfullscreen="allowfullscreen"></iframe>
          <button @click="isModalViewed(event)">닫기</button>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movie'
const isModalView = ref(false)

const isModalViewed = function (event) {
  this.isModalView = !this.isModalView
}

defineProps({
  movie: Object
})

const movieStore = useMovieStore()

const youtubeTrailer = computed(() => {
    return movieStore.movie.trailer_key
})

</script>

<style scoped>
.modal-wrap {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  z-index: 100;
}
/* modal or popup */
.modal-container {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 760px;
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  box-sizing: border-box;
}

</style>