from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.serializers.profile import AgentProfileSerializer
from common.middleware.authentication import JWTAuthentication
#获取与更新探员信息
class AgentProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = AgentProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = AgentProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "更新成功"})
        return Response(serializer.errors, status=400)
