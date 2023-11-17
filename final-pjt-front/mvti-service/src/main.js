import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)

app.use(createPinia())

library.add(faUserSecret)

app.use(router)

app.mount('#app')

// 로컬스토리지에 저장하는거 추가해야 될수도