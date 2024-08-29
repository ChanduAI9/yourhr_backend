from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .models import Resume
from .serializers import JobSeekerSerializer, ResumeSerializer
from rest_framework.permissions import AllowAny
from rest_framework import serializers


class JobSeekerCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = JobSeekerSerializer
    permission_classes = [AllowAny]

class ResumeUploadView(APIView):
    def post(self, request, format=None):
        print("FILES RECEIVED:", request.FILES)  # Check if files are received

        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save()
            print("Resume created with file path:", resume.resume_file.path)  # Debugging: Check file path
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)