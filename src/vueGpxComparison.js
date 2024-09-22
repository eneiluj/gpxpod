import { createApp } from 'vue'
import ComparisonContent from './ComparisonContent.vue'
import '../css/maplibre.scss'

const app = createApp(ComparisonContent)
app.mixin({ methods: { t, n } })
app.mount('#content')
