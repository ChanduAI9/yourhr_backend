from django.urls import path
from .views import JobSeekerCreateView, ResumeUploadView

urlpatterns = [
    path('signup/', JobSeekerCreateView.as_view(), name='signup'),
    path('upload-resume/', ResumeUploadView.as_view(), name='upload-resume'),
]
