from django.db import models  # 导入Django模型模块，用于定义数据库模型

class Agent(models.Model):
    """
    代理用户（探员/管理员）模型类
    用于存储用户基本信息、角色、状态及时间戳等数据
    """
    
    # 定义角色选择常量（元组格式：(数据库存储值, 展示值)）
    ROLE_CHOICES = (
        ('agent', '探员'),    # 普通用户角色，存储为'agent'，展示为'探员'
        ('admin', '管理员'),  # 管理员角色，存储为'admin'，展示为'管理员'
    )
    
    # ------------------------- 基础信息字段 -------------------------
    username = models.CharField(
        max_length=50,       # 最大长度50字符
        unique=True,         # 唯一约束，不允许重复用户名
        verbose_name='用户名' # 字段描述（后台管理显示）
    )
    password = models.CharField(
        max_length=255,      # 最大长度255字符（建议配合密码哈希使用）
        verbose_name='密码'
    )
    contact = models.CharField(
        max_length=100,      # 最大长度100字符
        blank=True,          # 允许为空（表单提交时可不填）
        verbose_name='联系方式'
    )
    free_time = models.CharField(
        max_length=100,      # 最大长度100字符
        blank=True,          # 允许为空
        verbose_name='空闲时间'
    )
    personal_info = models.TextField(
        blank=True,          # 允许为空
        verbose_name='个人简介'
    )
    wx_qrcode = models.CharField(
        max_length=255,      # 最大长度255字符（适合存储URL或路径）
        blank=True,          # 允许为空
        verbose_name='微信二维码'
    )
    
    # ------------------------- 权限与状态字段 -------------------------
    role = models.CharField(
        max_length=10,       # 最大长度10字符（对应ROLE_CHOICES中的存储值长度）
        choices=ROLE_CHOICES,# 限制只能选择ROLE_CHOICES中的值
        default='agent',     # 默认角色为'探员'
        verbose_name='角色'
    )
    status = models.BooleanField(
        default=True,        # 默认状态为True（启用）
        verbose_name='状态'
    )
    
    # ------------------------- 自动生成字段 -------------------------
    created_time = models.DateTimeField(
        auto_now_add=True,   # 仅在创建时自动填充当前时间
        verbose_name='创建时间'
    )
    updated_time = models.DateTimeField(
        auto_now=True,       # 每次保存时自动更新为当前时间
        verbose_name='更新时间'
    )
    
    # ------------------------- 模型元数据 -------------------------
    class Meta:
        db_table = 'agents'          # 指定数据库表名（默认为应用名_类名小写）
        verbose_name = '代理用户'     # 单数形式名称（后台管理显示）
        verbose_name_plural = '代理用户'  # 复数形式名称（后台管理显示）
        ordering = ['-created_time'] # 默认排序：按创建时间倒序
    
    # ------------------------- 模型方法 -------------------------
    def __str__(self):
        """
        返回模型对象的字符串表示（用于调试和后台显示）
        """
        return f"{self.username} ({self.role})"  # 格式：用户名（角色）