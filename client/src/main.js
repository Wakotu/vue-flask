/*
 * @Author: Axiuxiu
 * @Date: 2022-02-26 20:06:05
 * @LastEditTime: 2022-02-28 14:47:06
 * @Description: 入口文件
 */
import Vue from 'vue'
import App from './App.vue'
// 使用vue-router和vuex
import router from './router';
import store from './store';
// 使用element-ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 使用配置好的axios
import axios from './http';

Vue.config.productionTip = false

Vue.use(ElementUI);

Vue.prototype.$axios=axios;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
