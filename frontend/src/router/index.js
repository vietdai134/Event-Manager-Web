import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import EventCreatedView from '@/views/EventCreatedView.vue'
import EventPublicView from '@/views/EventPublicView.vue'
import EventRegisteredView from '@/views/EventRegisteredView.vue'
import EventPastView from '@/views/EventPastView.vue'
import DetailEvent from '@/views/EventDetailView.vue'
import InfoUserView from '@/views/InfoUserView.vue'
import createEvent from '@/views/createEvent.vue'

import Login from '@/views/Login.vue'
import ListUserView from '@/views/ListUserView.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/About',
    name: 'About',
    component:AboutView
  },
  {
    path:'/Events-Public',
    name:'EventsPublic',
    component:EventPublicView
  },
  {
    path: '/Events-Public/:id',
    name: 'DetailEventPublic',
    component: DetailEvent,
    props: true, 
  },
  {
    path:'/Events-Created',
    name:'EventsCreated',
    component:EventCreatedView
  },
  
  {
    path: '/Events-Created/:id',
    name: 'DetailEventsCreated',
    component: DetailEvent,
    props: true, 
  },

  {
    path: '/Events-Created/:id/listUser',
    name: 'ListUserView',
    component: ListUserView,
    props: true, 
  },

  {
    path:'/Events-Registered',
    name:'EventsRegistered',
    component:EventRegisteredView
  },
  {
    path: '/Events-Registered/:id',
    name: 'DetailEventRegistered',
    component: DetailEvent,
    props: true, 
  },
  {
    path:'/Events-Past',
    name:'EventsPast',
    component:EventPastView
  },
  
  {
    path: '/Events-Past/:id',
    name: 'DetailEventsPast',
    component: DetailEvent,
    props: true, 
  },
  {
    path:'/Info-User',
    name:'InfoUser',
    component:InfoUserView
  },
  {
    path:'/Login',
    name:'Login',
    component:Login
  },
  {
    path:'/Create_Event',
    name:'createEvent',
    component:createEvent
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
