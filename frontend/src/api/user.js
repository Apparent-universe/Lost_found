import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api/users', // 根据你的后端API路径进行配置
  timeout: 10000, // 超时时间
});

// 请求拦截器
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default {
  // 用户登录
  login(credentials) {
    return apiClient.post('/login/', credentials);
  },
  // 用户注册
  register(userData) {
    return apiClient.post('/register/', userData);
  },
  // 获取或更新用户资料
  profile(data = null) {
    if (data) {
      return apiClient.put('/profile/', data);
    } else {
      return apiClient.get('/profile/');
    }
  },
  // 修改密码
  changePassword(passwordData) {
    return apiClient.post('/change-password/', passwordData);
  },
  // 上传二维码
  uploadQRCode(formData) {
    return apiClient.post('/upload_qrcode/', formData);
  }
};