<!-- HelloWorld.vue -->
<!-- 这是一个使用 Vue 3 <script setup> 语法糖的组件 -->
<!-- 该组件展示了如何接收 props、使用响应式数据和处理事件 -->

<script setup>
// 导入 Vue 3 的 ref 函数，用于创建响应式数据
import { ref } from 'vue'

// 定义组件接收的 props
// 这里接收一个名为 msg 的 prop，类型为 String
defineProps({
  msg: String,
})

// 使用 ref 创建一个响应式变量 count，初始值为 0
// ref 创建的变量需要通过 .value 访问，但在模板中可以直接使用
const count = ref(0)
</script>

<template>
  <div>
    <!-- 显示从父组件传递的 msg prop -->
    <h1>{{ msg }}</h1>

    <div class="card">
      <!-- 点击按钮时，count 值会增加 -->
      <!-- 在模板中可以直接使用 ref 变量，无需 .value -->
      <button type="button" @click="count++">count is {{ count }}</button>
      <p>
        Edit
        <code>components/HelloWorld.vue</code> to test HMR
      </p>
    </div>

    <!-- 以下是一些链接，提供 Vue 和 Vite 的学习资源 -->
    <p>
      Check out
      <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank">create-vue</a>, the official Vue + Vite
      starter
    </p>
    <p>
      Learn more about IDE Support for Vue in the
      <a href="https://vuejs.org/guide/scaling-up/tooling.html#ide-support" target="_blank">Vue Docs Scaling up
        Guide</a>.
    </p>

    <!-- 提示信息，使用了 scoped 样式 -->
    <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
  </div>
</template>

<style scoped>
/* 使用 scoped 属性确保样式只应用于当前组件 */
/* 该类用于设置提示文本的颜色为灰色 */
.read-the-docs {
  color: #888;
}
</style>
