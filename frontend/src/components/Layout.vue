<template>
  <!-- 整体容器，设置最小高度为视口高度，确保内容撑满屏幕 -->
  <el-container style="min-height: 100vh">
    <!-- 左侧边栏：固定宽度200px，包含导航菜单 -->
    <el-aside width="200px">
      <!-- Element UI菜单组件，默认激活当前路由对应的菜单项 -->
      <el-menu :default-active="$route.path" router class="el-menu-vertical-demo">
        <!-- 开启路由模式，菜单项点击自动跳转 -->
        <!-- 绑定当前路由路径，自动高亮对应菜单项 -->
        <!-- 首页菜单项，index对应路由路径 -->
        <el-menu-item index="/">
          <span>首页</span>
        </el-menu-item>
        <!-- 失物招领菜单项 -->
        <el-menu-item index="/lost">
          <span>失物招领</span>
        </el-menu-item>
        <!-- 寻物启事菜单项 -->
        <el-menu-item index="/found">
          <span>寻物启事</span>
        </el-menu-item>
        <!-- 我的发布菜单项 -->
        <el-menu-item index="/my-items">
          <span>我的发布</span>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <!-- 右侧主体内容容器 -->
    <el-container>
      <!-- 顶部导航栏 -->
      <el-header>
        <!-- 左侧Logo区域 -->
        <div class="logo">校园失物招领平台</div>

        <!-- 右侧用户信息区域 -->
        <div class="user-info">
          <!-- 已登录状态：显示用户下拉菜单 -->
          <el-dropdown v-if="userStore.token">
            <span class="el-dropdown-link">
              <!-- 显示用户名，若未登录则显示“用户” -->
              <div class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center mr-2">
                <i class="el-icon-user text-gray-500"></i>
              </div>
              <div>{{ username }}</div>
              <!-- 显示当前登录用户名 -->
              <i class="el-icon-arrow-down el-icon--right"></i> <!-- 下拉箭头图标 -->
            </span>
            <!-- 下拉菜单内容 -->
            <template #dropdown>
              <el-dropdown-item @click="$router.push('/profile')">个人中心</el-dropdown-item>
              <el-dropdown-item divided @click="logout">退出登录</el-dropdown-item> <!-- divided添加分割线 -->
            </template>
          </el-dropdown>

          <!-- 未登录状态：显示登录按钮 -->
          <el-button v-else @click="$router.push('/login')">登录</el-button>
        </div>
      </el-header>

      <!-- 主内容区域，渲染当前路由对应的组件 -->
      <el-main>
        <router-view />
      </el-main>

      <!-- 底部页脚 -->
      <el-footer>
        <div class="footer">校园失物招领平台 © 2023</div>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script setup>
// 引入用户状态管理模块（Pinia或Vuex）
import { useUserStore } from '@/store/user';
import { watch, computed } from 'vue';

// 获取用户状态存储实例
const userStore = useUserStore();
const username = computed(() => userStore.user?.username || '');
// 退出登录功能
function logout() {
  userStore.logout(); // 调用状态管理中的退出方法（清除用户信息、token等）
  // 使用window.location强制跳转，确保清除前端路由缓存
  window.location.href = '/login';
}

// 添加调试日志，监听 userStore.user 的变化
watch(
  () => userStore.user,
  (newValue, oldValue) => {
    console.log('userStore.user changed:', { oldValue, newValue });
  }
);
</script>

<style scoped>
/* 顶部导航栏样式 */
.el-header {
  background-color: #4aadeb;
  /* Element UI主色调（蓝色） */
  color: white;
  /* 文字颜色 */
  line-height: 60px;
  /* 行高控制导航栏高度 */
  display: flex;
  /* 使用Flex布局 */
  justify-content: space-between;
  /* 内容左右两端对齐 */
  align-items: center;
  /* 垂直居中对齐 */
  padding: 0 20px;
  /* 左右内边距 */
  z-index: 1000;
  /* 提高导航栏的层级 */
}

/* Logo样式 */
.logo {
  font-size: 24px;
  /* 字体大小 */
  font-weight: bold;
  /* 字体加粗 */
}

/* 左侧边栏样式 */
.el-aside {
  background-color: #f5f7fa;
  /* 浅灰色背景 */
}

/* 垂直菜单样式（非折叠状态） */
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 100%;
  /* 宽度占满父容器 */
  min-height: 40px;
  /* 最小高度 */
}

/* 底部页脚样式 */
.footer {
  text-align: center;
  /* 文字居中对齐 */
  padding: 20px;
  /* 内边距 */
  color: #666;
  /* 深灰色文字 */
}

/* 修改下拉触发区域的样式 */
.el-dropdown-link {
  text-decoration: none;
  /* 移除下划线 */
  color: #333;
  /* 修改文字颜色 */
  cursor: pointer;
}

.user-info {
  display: flex;
  /* 或 block */
  align-items: center;
  widows: 100%;
  /* 使用户信息区域占满剩余空间 */
  height: 40px;
  /* 设置显式高度 */
}
</style>