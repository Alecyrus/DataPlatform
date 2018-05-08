import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import MainView from '@/components/MainView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Nevigator',
      component: MainView,
      children: [
        {
          path: '',
          component: Home
        }
      ]
    }
  ]
})
