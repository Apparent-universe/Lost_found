"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # 将所有以 /admin/ 开头的请求转发到 Django 内置的管理后台
    path("users/", include('users.urls')),
    # 将所有以 /users/ 开头的请求转发到 users 应用的 URL 配置
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 配置用户上传文件（如图片、视频）的访问路径

# Django 按顺序检查每个 path() 定义
# 一旦找到匹配前缀，就将剩余路径传递给对应的应用处理

# 可以使用 <type:name> 语法捕获路径中的变量
# path('articles/<int:year>/', views.year_archive),
# 请求 /articles/2023/ → year_archive 视图会收到 year=2023 参数
# 支持的类型包括：str、int、slug、uuid 等