import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import router from './router';
import { createPinia, defineStore } from 'pinia';
import { useUserStore } from './store/user.js';

import axios from 'axios';

// 配置 axios
axios.defaults.baseURL = '/api'; // 根据你的后端API路径进行配置
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

const pinia = createPinia();
const app = createApp(App);
app.use(ElementPlus);
app.use(router);
app.use(pinia);
app.config.globalProperties.$axios = axios;
app.mount('#app')