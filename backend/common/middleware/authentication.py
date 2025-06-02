from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from users.models.agent import Agent
from rest_framework.exceptions import AuthenticationFailed

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token过期")
        except jwt.DecodeError:
            raise AuthenticationFailed("Token无效")
        agent = Agent.objects.get(id=payload['id'])
        return (agent, None)
