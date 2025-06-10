from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.agent import Agent
from users.serializers.agent import AgentLoginSerializer
from django.contrib.auth.hashers import check_password
import jwt
from django.conf import settings

class LoginView(APIView):
    """
    处理代理用户登录的API视图
    """
    def post(self, request):
        """
        处理登录请求的POST方法
        """
        # 初始化序列化器并验证请求数据
        serializer = AgentLoginSerializer(data=request.data)
        
        # 检查序列化器是否通过验证
        if serializer.is_valid():
            # 从验证后的数据中获取用户名和密码
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            try:
                # 尝试从数据库中获取指定用户名的代理用户
                agent = Agent.objects.get(username=username)
                
                # 验证密码是否正确
                if check_password(password, agent.password):
                    # 密码正确，生成JWT令牌
                    token = jwt.encode(
                        # 令牌包含用户ID和角色信息
                        {"id": agent.id, "role": agent.role},
                        # 使用Django设置中的SECRET_KEY作为签名密钥
                        settings.SECRET_KEY,
                        # 指定HMAC-SHA256哈希算法
                        algorithm="HS256"
                    )
                    
                    # 构建包含令牌和角色的响应
                    response = Response({
                        "token": token,
                        "role": agent.role
                    })
                    
                    # 打印响应数据（调试用）
                    print(response.data)
                    
                    # 返回成功响应
                    return response
                else:
                    # 密码错误，返回401未授权响应
                    return Response({"error": "密码错误"}, status=status.HTTP_401_UNAUTHORIZED)
            except Agent.DoesNotExist:
                # 用户不存在，返回404未找到响应
                return Response({"error": "用户不存在"}, status=status.HTTP_404_NOT_FOUND)
        
        # 序列化器验证失败，返回400错误请求响应
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
