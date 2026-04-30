from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'contact')
    search_fields = ('title', 'description', 'contact_name', 'contact_last_name')
    ordering = ('title', 'contact')

admin.site.register(Task, TaskAdmin)
