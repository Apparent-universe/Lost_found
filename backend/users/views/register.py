from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers.agent import AgentRegisterSerializer

class RegisterView(APIView):
    """
    处理代理用户注册的API视图
    """
    def post(self, request):
        """
        处理注册请求的POST方法
        """
        # 初始化序列化器并传入请求数据
        serializer = AgentRegisterSerializer(data=request.data)
        
        # 验证请求数据是否符合序列化器定义的规则
        if serializer.is_valid():
            # 验证通过，保存新用户到数据库
            # 序列化器会自动处理密码哈希和字段验证
            serializer.save()
            
            # 返回成功响应，包含自定义消息和201状态码
            return Response({"message": "注册成功"}, status=status.HTTP_201_CREATED)
        
        # 验证失败，返回包含错误详情的响应和400状态码
        # 错误信息由序列化器自动生成，包含每个字段的具体错误
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
