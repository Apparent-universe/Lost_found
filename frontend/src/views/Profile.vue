<template>
  <div class="profile-container">
    <el-card class="profile-card">
      <h2>个人中心</h2>
      <el-form label-width="100px" class="profile-form">
        <el-form-item label="用户名">
          <el-input v-model="user.username" disabled />
        </el-form-item>
        <el-form-item label="联系方式">
          <el-input v-model="user.contact" />
        </el-form-item>
        <el-form-item label="空闲时间">
          <el-input v-model="user.free_time" />
        </el-form-item>
        <el-form-item label="个人简介">
          <el-input v-model="user.personal_info" type="textarea" :rows="3" />
        </el-form-item>
        <el-form-item label="微信二维码">
          <ImageUploader
            :current-image="user.wx_qrcode"
            @update:imageUrl="(url) => user.wx_qrcode = url"
          />
        </el-form-item>
        <el-form-item label="角色">
          <el-input :value="user.role === 'agent' ? '探员' : '管理员'" disabled />
        </el-form-item>
        <el-form-item label="状态">
          <el-switch v-model="user.status" disabled />
        </el-form-item>
        <el-form-item label="注册时间">
          <el-input :value="formatDate(user.created_time)" disabled />
        </el-form-item>
        <el-form-item label="最近更新">
          <el-input :value="formatDate(user.updated_time)" disabled />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="saveProfile">保存修改</el-button>
          <el-button @click="changePassword">修改密码</el-button>
          <el-button @click="logout">退出登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted, watchEffect } from 'vue';
import { useUserStore } from '@/store/user';
import userApi from '@/api/user';

// 获取用户存储
const userStore = useUserStore();

// 用户数据 - 使用计算属性直接从store获取
const user = ref({});

// 加载用户资料
const loadUserProfile = async () => {
  try {
    // 直接使用store中的用户数据
    if (userStore.isAuthenticated && userStore.user) {
      user.value = { ...userStore.user };
      return;
    }

    // 如果store中没有用户数据，则从API获取
    const response = await userApi.profile();
    const userData = response.data;
    userStore.login(userData, localStorage.getItem('token'));
    user.value = { ...userData };
  } catch (error) {
    alert('加载用户信息失败');
    console.error(error);
  }
};

// 监听用户数据变化并自动更新store
watchEffect(() => {
  if (user.value && userStore.isAuthenticated) {
    userStore.updateUserInfo(user.value);
  }
});

// 保存用户资料
const saveProfile = async () => {
  try {
    // 调用API更新用户资料
    const response = await userApi.profile(user.value);
    
    // 直接更新store中的用户信息
    userStore.updateUserInfo(response.data);
    
    // 更新本地用户数据
    user.value = { ...response.data };
    
    alert('资料更新成功');
  } catch (error) {
    alert('更新失败，请检查输入内容');
    console.error(error);
  }
};

// 修改密码
const changePassword = () => {
  const newPassword = prompt('请输入新密码');
  if (newPassword) {
    userApi.changePassword({ password: newPassword })
      .then(() => {
        alert('密码修改成功');
      })
      .catch((error) => {
        alert('密码修改失败');
        console.error(error);
      });
  }
};

// 登出
const logout = () => {
  userStore.logout();
  window.location.href = '/login';
};

// 日期格式化
const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return `${date.getFullYear()}-${(date.getMonth()+1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
};

// 在组件挂载时加载用户资料
onMounted(() => {
  loadUserProfile();
});
</script>

<script>
import ImageUploader from '@/components/ImageUploader.vue';

export default {
  components: {
    ImageUploader
  },
  name: 'Profile'
};
</script>