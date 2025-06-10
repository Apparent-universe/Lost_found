from rest_framework.authentication import BaseAuthentication  # 导入DRF基础认证类
import jwt  # 导入JWT处理库
from django.conf import settings  # 导入Django配置
from users.models.agent import Agent  # 导入用户模型
from rest_framework.exceptions import AuthenticationFailed  # 导入认证失败异常类

class JWTAuthentication(BaseAuthentication):
    """
    JWT认证类，用于验证请求中的JWT令牌并获取用户对象
    继承自DRF的BaseAuthentication，需实现authenticate方法
    """
    def authenticate(self, request):
        """
        认证方法，DRF会自动调用此方法验证请求
        Args:
            request: 当前HTTP请求对象
        Returns:
            tuple: (用户对象, 令牌) 或 None（认证失败时）
        """
        # 1. 从请求头中提取令牌
        # 预期格式：Authorization: Bearer <token字符串>
        token = request.headers.get('Authorization')
        
        # 若请求头中没有令牌，返回None（表示需要其他认证方式或匿名访问）
        if not token:
            return None
        
        # 2. 解析和验证令牌
        try:
            # 使用settings中的SECRET_KEY作为密钥解析令牌
            # algorithms指定允许的签名算法（需与生成令牌时一致）
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            # 捕获令牌过期异常
            raise AuthenticationFailed("Token过期")  # 抛出认证失败异常，状态码401
        except jwt.DecodeError:
            # 捕获令牌解析错误（如签名无效、格式错误）
            raise AuthenticationFailed("Token无效")  # 抛出认证失败异常，状态码401
        
        # 3. 根据令牌中的用户ID查询数据库
        try:
            # 从令牌负载（payload）中获取用户ID（需与生成令牌时的字段一致）
            agent = Agent.objects.get(id=payload['id'])
        except Agent.DoesNotExist:
            # 用户不存在时抛出认证失败异常
            raise AuthenticationFailed("用户不存在")
        
        # 4. 认证成功，返回用户对象和令牌（令牌可留空或用于其他场景）
        return (agent, None)