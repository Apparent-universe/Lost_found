from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models.agent import Agent
from users.serializers.agent import AgentLoginSerializer
from django.contrib.auth.hashers import check_password
import jwt
from django.conf import settings

class LoginView(APIView):
    def post(self, request):
        serializer = AgentLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                agent = Agent.objects.get(username=username)
                if check_password(password, agent.password):
                    token = jwt.encode(
                        {"id": agent.id, "role": agent.role},
                        settings.SECRET_KEY,
                        algorithm="HS256"
                    )
                    return Response({
                        "token": token,
                        "role": agent.role
                    })
                else:
                    return Response({"error": "密码错误"}, status=status.HTTP_401_UNAUTHORIZED)
            except Agent.DoesNotExist:
                return Response({"error": "用户不存在"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
