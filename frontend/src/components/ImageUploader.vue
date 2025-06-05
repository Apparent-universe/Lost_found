<template>
  <div class="image-uploader">
    <el-upload
      action=""
      :http-request="uploadImage"
      :show-file-list="false"
      :before-upload="beforeUpload"
      :on-success="handleSuccess"
      :on-error="handleError"
      :limit="1"
      accept="image/*"
    >
      <el-button type="primary">点击上传</el-button>
    </el-upload>
    
    <div v-if="imageUrl" class="image-preview">
      <img :src="imageUrl" alt="预览" class="preview-image" />
    </div>
    
    <p v-if="uploadStatus" class="upload-status" :class="{ 'success': uploadSuccess, 'error': !uploadSuccess }">
      {{ uploadStatus }}
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElUpload, ElButton, ElMessage } from 'element-plus';
import { axios } from '@/api/user';

// 定义props
const props = defineProps({
  // 当前图片URL
  currentImage: {
    type: String,
    default: ''
  }
});

// 定义emit
const emit = defineEmits(['update:imageUrl']);

// 图片URL
const imageUrl = ref(props.currentImage);
// 上传状态
const uploadStatus = ref('');
// 上传成功标志
const uploadSuccess = ref(false);

// 验证文件类型和大小
const beforeUpload = (file) => {
  const isValidType = file.type.startsWith('image/');
  const isValidSize = file.size / 1024 / 1024 < 5; // 限制为5MB
  
  if (!isValidType) {
    ElMessage.error('只能上传图片文件!');
    return false;
  }
  
  if (!isValidSize) {
    ElMessage.error('图片大小不能超过5MB!');
    return false;
  }
  
  uploadStatus.value = '正在上传...';
  uploadSuccess.value = false;
  
  return true;
};

// 自定义上传方法
const uploadImage = async ({ file }) => {
  try {
    // 创建表单数据
    const formData = new FormData();
    formData.append('image', file);
    
    // 调用API上传图片
    const response = await axios.post('/users/upload_qrcode/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    
    // 更新图片URL
    imageUrl.value = response.data.qrcode_url;
    uploadStatus.value = '上传成功';
    uploadSuccess.value = true;
    
    // 触发事件，将新URL传递给父组件
    emit('update:imageUrl', imageUrl.value);
    
    return response;
  } catch (error) {
    console.error('上传失败:', error);
    uploadStatus.value = '上传失败';
    uploadSuccess.value = false;
    throw error;
  }
};

// 上传成功回调
const handleSuccess = () => {
  ElMessage.success('图片上传成功');
};

// 上传失败回调
const handleError = () => {
  ElMessage.error('图片上传失败');
};
</script>

<script>
export default {
  components: {
    ElUpload,
    ElButton
  },
  props: ['currentImage'],
  name: 'ImageUploader'
};
</script>

<style scoped>
.image-uploader {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.image-preview {
  margin-top: 20px;
  border: 1px solid #e4e4e4;
  padding: 10px;
  border-radius: 8px;
  max-width: 300px;
}

.preview-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.upload-status {
  margin-top: 15px;
  font-size: 14px;
}

.upload-status.success {
  color: #13ce66;
}

.upload-status.error {
  color: #ff4949;
}
</style>