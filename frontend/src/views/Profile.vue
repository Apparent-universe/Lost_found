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

<script>
import { useUserStore } from '@/store/user';
import userApi from '@/api/user';
import ImageUploader from '@/components/ImageUploader.vue';

export default {
  components: {
    ImageUploader
  },
  data() {
    return {
      user: {}
    };
  },
  created() {
    this.loadUserProfile();
  },
  methods: {
    async loadUserProfile() {
      try {
        // 从Pinia store获取用户信息或调用API
        const userStore = useUserStore();
        
        if (userStore.isAuthenticated && userStore.user) {
          this.user = { ...userStore.user };
        } else {
          const response = await userApi.profile();
          const userData = response.data;
          userStore.login(userData, localStorage.getItem('token'));
          this.user = { ...userData };
        }
      } catch (error) {
        this.$message.error('加载用户信息失败');
        console.error(error);
      }
    },
    async saveProfile() {
      try {
        // 调用API更新用户资料
        const response = await userApi.profile(this.user);
        
        // 更新Pinia store中的用户信息
        const userStore = useUserStore();
        userStore.login(response.data, userStore.token);
        
        // 更新本地用户数据
        this.user = { ...response.data };
        
        this.$message.success('资料更新成功');
      } catch (error) {
        this.$message.error('更新失败，请检查输入内容');
        console.error(error);
      }
    },
    changePassword() {
      this.$prompt('请输入新密码', '修改密码', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        inputType: 'password'
      }).then(async ({ value }) => {
        if (value) {
          try {
            // 调用API修改密码
            await userApi.changePassword({ password: value });
            this.$message.success('密码修改成功');
          } catch (error) {
            this.$message.error('密码修改失败');
            console.error(error);
          }
        }
      }).catch(() => {
        // 取消操作
      });
    },
    logout() {
      const userStore = useUserStore();
      userStore.logout();
      this.$router.push('/login');
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return `${date.getFullYear()}-${(date.getMonth()+1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`;
    }
  }
};
</script>

<style scoped>
/* ... existing styles ... */
</style>