<template>
  <!-- 主容器 -->
  <div class="home-container">
    <!-- 顶部轮播图区域，使用Element UI的el-carousel组件 -->
    <el-carousel :interval="4000" type="card" height="300px">
      <!-- 循环渲染轮播图项，每项包含图片、标题和描述 -->
      <el-carousel-item v-for="(item, index) in slides" :key="index">
        <img :src="item.image" alt="slide" class="carousel-image" />
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
      </el-carousel-item>
    </el-carousel>

    <!-- 功能分类区域，使用栅格系统布局 -->
    <el-row :gutter="20" class="category-section">
      <!-- 失物招领卡片，点击导航到失物列表页 -->
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/lost')">
          <i class="el-icon-document"></i>
          <h4>失物招领</h4>
          <p>查看最新丢失物品信息</p>
        </el-card>
      </el-col>
      
      <!-- 寻物启事卡片，点击导航到寻物列表页 -->
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/found')">
          <i class="el-icon-document"></i>
          <h4>寻物启事</h4>
          <p>发布或查看寻物信息</p>
        </el-card>
      </el-col>
      
      <!-- 发布信息卡片，点击导航到发布表单页 -->
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/post')">
          <i class="el-icon-edit"></i>
          <h4>发布信息</h4>
          <p>发布新的失物或寻物信息</p>
        </el-card>
      </el-col>
      
      <!-- 我的发布卡片，点击导航到个人发布管理页 -->
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/my-items')">
          <i class="el-icon-user"></i>
          <h4>我的发布</h4>
          <p>管理您发布的所有信息</p>
        </el-card>
      </el-col>
    </el-row>

    <!-- 最新发布物品区域 -->
    <el-card class="recent-items">
      <h3>最新发布</h3>
      <!-- 使用栅格系统展示最新4条物品信息 -->
      <el-row :gutter="20">
        <el-col :span="6" v-for="(item, index) in recentItems" :key="index">
          <el-card class="item-card">
            <img :src="item.image" class="item-image" alt="item" />
            <div class="item-info">
              <h4>{{ item.title }}</h4>
              <p>{{ item.description }}</p>
              <div class="item-meta">
                <span>{{ item.type }}</span>
                <span>{{ item.date }}</span>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 轮播图数据：包含图片URL、标题和描述
const slides = [
  { image: 'https://via.placeholder.com/800x300?text=校园失物招领平台', title: '欢迎使用校园失物招领平台', description: '在这里您可以方便地查找或发布失物和寻物信息' },
  { image: 'https://via.placeholder.com/800x300?text=快速找到丢失物品', title: '快速找到丢失物品', description: '通过我们的平台，您可以快速浏览最新的失物信息' },
  { image: 'https://via.placeholder.com/800x300?text=发s布您的寻物启事', title: '发布您的寻物启事', description: '简单三步即可发布您的寻物信息，让更多人帮助您寻找' }
];

// 最新发布物品数据：包含图片、标题、描述、类型和日期
const recentItems = [
  { image: 'https://via.placeholder.com/300x200?text=钱包', title: '黑色钱包', description: '在图书馆二楼捡到黑色皮质钱包', type: '失物招领', date: '2023-09-15' },
  { image: 'https://via.placeholder.com/300x200?text=书包', title: '蓝色双肩包', description: '教学楼A区302教室发现蓝色双肩包', type: '失物招领', date: '2023-09-14' },
  { image: 'https://via.placeholder.com/300x200?text=钥匙', title: '一串钥匙', description: '实验楼一楼大厅服务台拾取', type: '失物招领', date: '2023-09-13' },
  { image: 'https://via.placeholder.com/300x200?text=手机', title: '红色手机壳iPhone', description: '操场跑道上捡到红色手机壳iPhone 13', type: '失物招领', date: '2023-09-12' }
];
</script>

<script>
// 组件配置：设置组件名称
export default {
  name: 'Home'
};
</script>

<style scoped>
/* 主容器样式 */
.home-container {
  padding: 20px;
}

/* 轮播图图片样式 */
.carousel-image {
  width: 100%;
  height: 300px;
  object-fit: cover;  /* 保持图片比例，覆盖容器 */
  border-radius: 8px; /* 圆角效果 */
}

/* 分类区域样式 */
.category-section {
  margin-top: 30px;
  margin-bottom: 30px;
}

/* 分类卡片样式 */
.category-card {
  cursor: pointer;    /* 鼠标悬停时显示手型 */
  text-align: center; /* 内容居中 */
  padding: 20px;
  transition: all 0.3s ease; /* 添加过渡动画 */
}

/* 分类卡片悬停效果 */
.category-card:hover {
  transform: translateY(-5px); /* 向上浮动5px */
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1); /* 添加阴影 */
}

/* 分类卡片图标样式 */
.category-card i {
  font-size: 48px;
  color: #409EFF; /* Element UI主色调 */
  margin-bottom: 10px;
}

/* 最新发布区域样式 */
.recent-items {
  padding: 20px;
}

/* 物品卡片样式 */
.item-card {
  cursor: pointer;
  transition: all 0.3s ease;
}

/* 物品卡片悬停效果 */
.item-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

/* 物品图片样式 */
.item-image {
  width: 100%;
  height: 200px;
  object-fit: cover; /* 保持图片比例，覆盖容器 */
}

/* 物品信息区域样式 */
.item-info {
  padding: 15px;
}

/* 物品元数据样式 */
.item-meta {
  display: flex;
  justify-content: space-between; /* 两端对齐 */
  color: #888; /* 灰色文字 */
  font-size: 12px;
  margin-top: 10px;
}
</style>