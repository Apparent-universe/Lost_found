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

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/store/user';
import userApi from '@/api/user';
import { jwtDecode } from 'jwt-decode'; // 修复导入方式，使用命名导出
import { useRouter } from 'vue-router';

// 表单数据
const loginForm = ref({
  username: '',
  password: ''
});

const router = useRouter();

// 提交登录表单
const onSubmit = async () => {
  try {
    console.log('提交登录表单');
    // 使用API模块登录
    const response = await userApi.login(loginForm.value);

    // 获取token并解析用户信息
    const token = response.data.token;
    const decodedToken = jwtDecode(token); // 使用 jwtDecode 解析 JWT 令牌
    const userData = {
      id: decodedToken.id, // 从令牌中提取用户ID
      role: decodedToken.role, // 从令牌中提取用户角色
      username: loginForm.value.username
    };

    // 使用Pinia store保存用户信息
    const userStore = useUserStore();
    userStore.login(userData, token);
    console.log('登录成功', userData);
    console.log('Token:', token);
    router.push('/');
  } catch (error) {
    // 显示错误提示
    alert('登录失败，请检查用户名和密码');
    console.error(error);
  }
};

// 取消登录
const onCancel = () => {
  window.location.href = '/';
};
</script>

<script>
export default {
  name: 'Login'
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f2f5;
}

.login-form {
  width: 300px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.register-link {
  text-align: center;
  margin-top: 10px;
}

.register-link a {
  color: #409eff;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}
</style>