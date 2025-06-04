<template>
  <el-container style="min-height: 100vh">
    <el-aside width="200px">
      <el-menu
        :default-active="$route.path"
        router
        class="el-menu-vertical-demo"
      >
        <el-menu-item index="/">
          <span>首页</span>
        </el-menu-item>
        <el-menu-item index="/lost">
          <span>失物招领</span>
        </el-menu-item>
        <el-menu-item index="/found">
          <span>寻物启事</span>
        </el-menu-item>
        <el-menu-item index="/my-items">
          <span>我的发布</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header>
        <div class="logo">校园失物招领平台</div>
        <div class="user-info">
          <el-dropdown v-if="userStore.user">
            <span class="el-dropdown-link">
              {{ userStore.user.name }}
              <i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <template #dropdown>
              <el-dropdown-item @click="$router.push('/profile')">个人中心</el-dropdown-item>
              <el-dropdown-item divided @click="logout">退出登录</el-dropdown-item>
            </template>
          </el-dropdown>
          <el-button v-else @click="$router.push('/login')">登录</el-button>
        </div>
      </el-header>

      <el-main>
        <router-view />
      </el-main>

      <el-footer>
        <div class="footer">校园失物招领平台 © 2023</div>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script setup>
import { useUserStore } from '@/store/user';

const userStore = useUserStore();

function logout() {
  userStore.logout();
  window.location.href = '/login'; // 用 window 确保刷新清缓存（可选）
}
</script>

<style scoped>
.el-header {
  background-color: #409EFF;
  color: white;
  line-height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.logo {
  font-size: 24px;
  font-weight: bold;
}

.el-aside {
  background-color: #f5f7fa;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 100%;
  min-height: 40px;
}

.footer {
  text-align: center;
  padding: 20px;
  color: #666;
}
</style>
