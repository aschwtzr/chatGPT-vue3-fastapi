import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import './index.css'
import { createRouter, createWebHashHistory } from 'vue-router'
import Chat from './components/Chat.vue'


const routes = [
    { path: '/', component: Chat },
    { path: '/chat', component: Chat },
  ]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')

