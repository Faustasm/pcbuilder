import Builder from '@/views/Builder.vue'
import RecommendationSystem from '@/views/RecommendationSystem.vue'
import Api from '@/views/Api.vue'
import About from '@/views/About.vue'
import Contacts from '@/views/Contacts.vue'

const routes = [
  {
    path: '/',
    name: 'Builder',
    component: Builder
  },
  {
    path: '/recommendation-system',
    name: 'RecommendationSystem',
    component: RecommendationSystem
  },
  {
    path: '/api',
    name: 'Api',
    component: Api
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts
  }
]

export default routes;
