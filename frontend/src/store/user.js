import { defineStore } from 'pinia';

const useUserStore = defineStore('user', {
  state: () => {
    // 获取存储的用户数据
    const storedUser = localStorage.getItem('user');
    const storedToken = localStorage.getItem('token');
    
    // 初始化用户数据，添加错误处理
    let user = null;
    if (storedUser) {
      try {
        user = JSON.parse(storedUser);
      } catch (error) {
        console.error('Failed to parse user data from localStorage:', error);
        // 解析失败时重置用户数据
        localStorage.removeItem('user');
      }
    }
    
    return {
      user,
      token: storedToken || null,
      isAuthenticated: !!storedToken,
    };
  },
  actions: {
    login(userData, token) {
      this.user = userData;
      this.token = token;
      this.isAuthenticated = true;
      localStorage.setItem('token', token);
      localStorage.setItem('user', JSON.stringify(userData));
      console.log('Login called with:', { userData, token }); // 关键日志
    },
    logout() {
      this.user = null;
      this.token = null;
      this.isAuthenticated = false;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    }
  },
  getters: {
    userId: (state) => {
      return state.user?.id;
    },
  },
});

export { useUserStore };