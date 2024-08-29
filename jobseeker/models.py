from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
# Create your models here.

class JobSeeker(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='jobseeker_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='jobseeker_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Resume(models.Model):
    job_seeker = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("Saving resume with file:", self.resume_file)
        super(Resume, self).save(*args, **kwargs)
        print("File saved to:", self.resume_file.path)