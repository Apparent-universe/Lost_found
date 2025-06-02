from django.db import models

class Agent(models.Model):
    ROLE_CHOICES = (('agent', '探员'), ('admin', '管理员'))
    
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    contact = models.CharField(max_length=100, blank=True)
    free_time = models.CharField(max_length=100, blank=True)
    personal_info = models.TextField(blank=True)
    wx_qrcode = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='agent')
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
