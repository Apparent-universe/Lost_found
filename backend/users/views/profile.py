from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers.profile import AgentProfileSerializer
from common.middleware.authentication import JWTAuthentication

# 获取与更新探员信息
class AgentProfileView(APIView):
    """
    处理探员个人信息的获取和更新的API视图
    - 仅认证用户可访问
    - 使用JWT进行身份验证
    """
    # 指定使用的认证类，负责验证请求中的令牌
    authentication_classes = [JWTAuthentication]
    # 指定权限类，确保只有经过认证的用户才能访问此视图
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        获取当前登录探员的个人信息
        """
        # 实例化序列化器，传入当前认证的用户对象
        # request.user 是经过 JWT 认证后解析出的用户对象
        serializer = AgentProfileSerializer(request.user)
        
        # 返回序列化后的用户数据（如用户名、邮箱等）
        return Response(serializer.data)

    def put(self, request):
        """
        更新当前登录探员的个人信息（部分更新）
        """
        # 实例化序列化器：
        # 1. request.user - 指定要更新的用户对象
        # 2. data=request.data - 传入请求中的新数据
        # 3. partial=True - 允许部分更新（不需要提供所有字段）
        serializer = AgentProfileSerializer(request.user, data=request.data, partial=True)
        
        # 验证输入数据的有效性（如字段类型、长度等）
        if serializer.is_valid():
            # 验证通过，保存更新
            serializer.save()
            
            # 返回成功消息
            return Response({"message": "更新成功"})
        
        # 验证失败，返回包含错误详情的响应
        return Response(serializer.errors, status=400)