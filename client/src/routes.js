import Builder from '@/views/Builder.vue'
import About from '@/views/About.vue'
import Contacts from '@/views/Contacts.vue'

const routes = [
  {
    path: '/',
    name: 'Builder',
    component: Builder
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

export default routes
