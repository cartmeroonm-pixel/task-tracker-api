from django.contrib import admin
from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    list_filter = ("owner",)  # filter by owner
    search_fields = ("name",)  # search by project name

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'owner', 'created_at')
    list_filter = ("project", "status", "owner")  # filters
    search_fields = ("title", "description")  # search by title and description
