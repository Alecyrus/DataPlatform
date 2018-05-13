import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Results from '@/components/Results'
import MainView from '@/components/MainView'
import Certificate from '@/components/Certificate'
import Smmary from '@/components/Smmary'
import Reports from '@/components/Reports'
import OpenSSL from '@/components/OpenSSL'
import Asn1 from '@/components/Asn1'
import Apple from '@/components/Apple'
import Microsoft from '@/components/Microsoft'
import GoogleCT from '@/components/GoogleCT'
import MozillaNss from '@/components/MozillaNss'
import RawData from '@/components/RawData'

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
          path:'certificate',
          component:Certificate,
          children: [
            {
              path: '', 
              component:Smmary,
            },
            {
              path: 'openssl', 
              component:OpenSSL,
            },
            {
              path: 'apple', 
              component:Apple,
            },
            {
              path: 'asn1', 
              component:Asn1,
            },
            {
              path: 'microsoft', 
              component:Microsoft,
            },
            {
              path: 'mozillanss', 
              component:MozillaNss,
            },
            {
              path: 'googlect', 
              component:GoogleCT,
            },
            {
              path: 'rawdata', 
              component:RawData,
            },
          ]
        }
      ]
    }
  ]
})
