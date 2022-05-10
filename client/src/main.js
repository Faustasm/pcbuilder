import Vue from 'vue'
import VueI18n from 'vue-i18n'
import VueRouter from 'vue-router'
import Multiselect from 'vue-multiselect'
import CountryFlag from 'vue-country-flag'
import App from './App.vue'
import messages from './lang'
import store from './store'
import routes from './routes'
import 'w3-css/w3.css'

Vue.config.productionTip = false

Vue.use(VueI18n)
Vue.use(VueRouter)
Vue.component('multiselect', Multiselect)
Vue.component('country-flag', CountryFlag)

const router = new VueRouter({
  routes,
  mode: 'history'
})

export const i18n = new VueI18n({
  locale: 'lt',
  fallbackLocale: 'lt',
  messages
})
new Vue({
  el: '#app',
  store,
  router,
  i18n,
  render: h => h(App)
})
