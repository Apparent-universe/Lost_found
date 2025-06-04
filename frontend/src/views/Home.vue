<template>
  <div class="home-container">
    <el-carousel :interval="4000" type="card" height="300px">
      <el-carousel-item v-for="(item, index) in slides" :key="index">
        <img :src="item.image" alt="slide" class="carousel-image" />
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
      </el-carousel-item>
    </el-carousel>

    <el-row :gutter="20" class="category-section">
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/lost')">
          <i class="el-icon-document"></i>
          <h4>失物招领</h4>
          <p>查看最新丢失物品信息</p>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/found')">
          <i class="el-icon-document"></i>
          <h4>寻物启事</h4>
          <p>发布或查看寻物信息</p>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/post')">
          <i class="el-icon-edit"></i>
          <h4>发布信息</h4>
          <p>发布新的失物或寻物信息</p>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card class="category-card" @click.native="$router.push('/my-items')">
          <i class="el-icon-user"></i>
          <h4>我的发布</h4>
          <p>管理您发布的所有信息</p>
        </el-card>
      </el-col>
    </el-row>

    <el-card class="recent-items">
      <h3>最新发布</h3>
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

<script>
export default {
  data() {
    return {
      slides: [
        { image: 'https://via.placeholder.com/800x300?text=校园失物招领平台', title: '欢迎使用校园失物招领平台', description: '在这里您可以方便地查找或发布失物和寻物信息' },
        { image: 'https://via.placeholder.com/800x300?text=快速找到丢失物品', title: '快速找到丢失物品', description: '通过我们的平台，您可以快速浏览最新的失物信息' },
        { image: 'https://via.placeholder.com/800x300?text=发布您的寻物启事', title: '发布您的寻物启事', description: '简单三步即可发布您的寻物信息，让更多人帮助您寻找' }
      ],
      recentItems: [
        { image: 'https://via.placeholder.com/300x200?text=钱包', title: '黑色钱包', description: '在图书馆二楼捡到黑色皮质钱包', type: '失物招领', date: '2023-09-15' },
        { image: 'https://via.placeholder.com/300x200?text=书包', title: '蓝色双肩包', description: '教学楼A区302教室发现蓝色双肩包', type: '失物招领', date: '2023-09-14' },
        { image: 'https://via.placeholder.com/300x200?text=钥匙', title: '一串钥匙', description: '实验楼一楼大厅服务台拾取', type: '失物招领', date: '2023-09-13' },
        { image: 'https://via.placeholder.com/300x200?text=手机', title: '红色手机壳iPhone', description: '操场跑道上捡到红色手机壳iPhone 13', type: '失物招领', date: '2023-09-12' }
      ]
    };
  }
};
</script>

<style scoped>
.home-container {
  padding: 20px;
}

.carousel-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
}

.category-section {
  margin-top: 30px;
  margin-bottom: 30px;
}

.category-card {
  cursor: pointer;
  text-align: center;
  padding: 20px;
  transition: all 0.3s ease;
}

.category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.category-card i {
  font-size: 48px;
  color: #409EFF;
  margin-bottom: 10px;
}

.recent-items {
  padding: 20px;
}

.item-card {
  cursor: pointer;
  transition: all 0.3s ease;
}

.item-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.item-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.item-info {
  padding: 15px;
}

.item-meta {
  display: flex;
  justify-content: space-between;
  color: #888;
  font-size: 12px;
  margin-top: 10px;
}
</style>