#探员信息序列化器
from rest_framework import serializers
from users.models.agent import Agent

class AgentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['contact', 'free_time', 'personal_info', 'wx_qrcode']
