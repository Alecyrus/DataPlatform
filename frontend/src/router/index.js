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
import CertifiAu from '@/components/CertifiAu'
import Sameseri from '@/components/Sameseri'
import Samepk from '@/components/Samepk'
import Samecn from '@/components/Samecn'
import Domains from '@/components/Domains'
import Ipv4 from '@/components/Ipv4'
import Analysis from '@/components/Analysis'
import About from '@/components/About'

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
          path: 'about',
          component: About
        },
        {
          path: 'analysis',
          component: Analysis
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
            {
              path: 'certifiau', 
              component:CertifiAu,
            },
            {
              path: 'certifiau', 
              component:CertifiAu,
            },
            {
              path: 'sameseri', 
              component:Sameseri,
            },
            {
              path: 'samepk', 
              component:Samepk,
            },
            {
              path: 'samecn', 
              component:Samecn,
            },
            {
              path: 'ipv4', 
              component:Ipv4,
            },
            {
              path: 'domains', 
              component:Domains,
            },
          ]
        }
      ]
    }
  ]
})
