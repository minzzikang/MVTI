import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)

library.add(faUserSecret)

app.use(router)

app.mount('#app')
