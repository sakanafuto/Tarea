from django.contrib import admin

from .models import Task, User

class TaskAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'caption', 'completed', 'user')

admin.site.register(Task, TaskAdmin)

admin.site.register(User)