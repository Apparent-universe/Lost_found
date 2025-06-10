from django.urls import path
from users.views.register import RegisterView
from users.views.login import LoginView
from users.views.profile import AgentProfileView
from users.views.upload_qrcode import UploadQRCodeView

# 定义用户模块的URL路由规则
urlpatterns = [
    # 注册路由：处理用户注册请求
    path('register/', RegisterView.as_view()),
    
    # 登录路由：处理用户登录请求
    path('login/', LoginView.as_view()),
    
    # 个人资料路由：获取和更新探员个人信息
    path('profile/', AgentProfileView.as_view()),
    
    # 二维码上传路由：处理微信二维码上传功能
    path('upload_qrcode/', UploadQRCodeView.as_view()),
]