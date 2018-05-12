import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Results from '@/components/Results'
import MainView from '@/components/MainView'
import Certificate from '@/components/Certificate'
import Smmary from '@/components/Smmary'
import Reports from '@/components/Reports'

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
        },
        {
          path: 'reports',
          component: Reports
        },
        {
          path:'results',
          component:Results,
        },
        {
          path:'certificate/:id',
          component:Certificate,
          children: [
            {
              path: '', 
              component:Smmary,
            }
          ]
        }
      ]
    }
  ]
})
