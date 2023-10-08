from django.db import models
from django.contrib.auth.models import User  # Import the User model from django.contrib.auth

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can add additional user-related fields here if needed
    # For example, profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate tasks with users

    def __str__(self):
        return self.title
