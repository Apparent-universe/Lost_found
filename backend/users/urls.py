from django.urls import path
from users.views.register import RegisterView
from users.views.login import LoginView
from users.views.profile import AgentProfileView
from users.views.upload_qrcode import UploadQRCodeView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', AgentProfileView.as_view()),
    path('upload_qrcode/', UploadQRCodeView.as_view()),
]
