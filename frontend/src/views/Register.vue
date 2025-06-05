<template>
  <div class="register-container">
    <el-form ref="form" :model="registerForm" label-width="80px" class="register-form">
      <h2>用户注册</h2>
      <el-form-item label="用户名">
        <el-input v-model="registerForm.username" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="registerForm.password" type="password" show-password />
      </el-form-item>
      <el-form-item label="确认密码">
        <el-input v-model="registerForm.confirmPassword" type="password" show-password />
      </el-form-item>
      <el-form-item label="角色">
        <el-select v-model="registerForm.role" placeholder="请选择角色">
          <el-option label="探员" value="agent" />
          <el-option label="管理员" value="admin" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">注册</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
      <div class="login-link">
        <p>已有账号？<a @click="$router.push('/login')">立即登录</a></p>
      </div>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import userApi from '@/api/user';

// 表单数据
const registerForm = ref({
  username: '',
  password: '',
  confirmPassword: '',
  role: 'agent'
});

// 提交注册表单
const onSubmit = async () => {
  if (registerForm.value.password !== registerForm.value.confirmPassword) {
    alert('两次输入的密码不一致');
    return;
  }
  
  try {
    // 调用注册API
    await userApi.register(registerForm.value);
    alert('注册成功，请登录');
    window.location.href = '/login';
  } catch (error) {
    alert('注册失败，请检查输入内容');
    console.error(error);
  }
};

// 取消注册
const onCancel = () => {
  window.location.href = '/';
};
</script>

<script>
export default {
  name: 'Register'
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f7fa;
}

.register-form {
  background-color: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);
  width: 400px;
}

.login-link {
  text-align: center;
  margin-top: 20px;
}

.login-link a {
  color: #409EFF;
  cursor: pointer;
}
</style>