import { createApp } from 'vue'
import App from './App.vue'
import '../css/maplibre.scss'

const app = createApp(App)
app.mixin({ methods: { t, n } })
app.mount('#content')
