from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers.agent import AgentRegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = AgentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "注册成功"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
