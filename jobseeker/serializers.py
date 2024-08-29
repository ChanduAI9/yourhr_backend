from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Resume

class JobSeekerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('resume_file',)

    def create(self, validated_data):
        resume = Resume.objects.create(**validated_data)
        return resume

