import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from common.middleware.authentication import JWTAuthentication
#上传微信二维码
class UploadQRCodeView(APIView):
    parser_classes = [MultiPartParser]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "未提供文件"}, status=400)
        
        file_name = f"qrcode_{request.user.id}.png"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        request.user.wx_qrcode = f"{settings.MEDIA_URL}{file_name}"
        request.user.save()
        return Response({"message": "上传成功", "url": request.user.wx_qrcode})
