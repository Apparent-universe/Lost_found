<template>
  <div class="login-container">
    <el-form ref="form" :model="loginForm" label-width="80px" class="login-form">
      <h2>用户登录</h2>
      <el-form-item label="用户名">
        <el-input v-model="loginForm.username" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginForm.password" type="password" show-password />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">登录</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
      <div class="register-link">
        <p>还没有账号？<a @click="$router.push('/register')">立即注册</a></p>
      </div>
    </el-form>
  </div>
</template>

<script>
import { useUserStore } from '@/store/user';
import userApi from '@/api/user';

export default {
  data() {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    async onSubmit() {
      try {
        // 使用API模块登录
        const response = await userApi.login(this.loginForm);
        
        // 获取token和用户信息
        const token = response.data.token;
        const userData = response.data.user;
        
        // 使用Pinia store保存用户信息
        const userStore = useUserStore();
        userStore.login(userData, token);
        
        // 跳转到首页
        this.$router.push('/');
      } catch (error) {
        this.$message.error('登录失败，请检查用户名和密码');
        console.error(error);
      }
    },
    onCancel() {
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
/* ... existing styles ... */
</style>