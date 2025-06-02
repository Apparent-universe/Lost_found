from rest_framework import serializers
from users.models.agent import Agent
from django.contrib.auth.hashers import make_password

class AgentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['username', 'password', 'role']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class AgentLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
