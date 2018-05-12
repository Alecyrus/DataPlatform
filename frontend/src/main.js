// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import router from './router'

import App from './App.vue'
import axios from 'axios';
import VueLocalStorage from 'vue-ls';
import iView from 'iview';
import 'iview/dist/styles/iview.css';
import '../mytheme/index.less';
import VueIziToast from 'vue-izitoast';
import 'izitoast/dist/css/iziToast.min.css';
import 'vue-awesome/icons'
import VueHighcharts from 'vue-highcharts';
import Highcharts from 'highcharts';

import loadMap from 'highcharts/modules/map';
import loadDrilldown from 'highcharts/modules/drilldown';
import loadHighchartsMore from 'highcharts/highcharts-more';
import Icon from 'vue-awesome/components/Icon'
import Vuebar from 'vuebar';
import Spinner from 'vue-spinkit'

loadMap(Highcharts);
loadDrilldown(Highcharts);
loadHighchartsMore(Highcharts);
Vue.use(VueHighcharts, { Highcharts });
Vue.component('Spinner', Spinner)
Vue.use(Vuebar);
Vue.component('awe-icon', Icon)
Vue.use(VueIziToast);





Vue.prototype.$highcharts = Highcharts;
//import VueParticles from 'vue-particles';
//Vue.use(VueParticles)
Vue.use(iView);
Vue.prototype.$request = axios;
Vue.use(VueLocalStorage);
Vue.config.productionTip = false;
require('vue2-animate/dist/vue2-animate.min.css')

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})


