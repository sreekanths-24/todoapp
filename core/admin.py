from django.contrib import admin
from .models import Task, UserProfile

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'due_date', 'completed', 'user')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'description', 'user__username')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
