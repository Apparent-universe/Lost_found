import { defineStore } from 'pinia';

const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
    isAuthenticated: false,
  }),
  actions: {
    login(userData, token) {
      this.user = userData;
      this.token = token;
      this.isAuthenticated = true;
      localStorage.setItem('token', token);
    },
    logout() {
      this.user = null;
      this.token = null;
      this.isAuthenticated = false;
      localStorage.removeItem('token');
    }
  },
  getters: {
    userId: (state) => {
      return state.user?.id;
    },
  },
});
export { useUserStore };