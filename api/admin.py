from django.contrib import admin
from .models import Project, Task



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    list_filter = ('owner',)  # фильтр по владельцу
    search_fields = ('name',)  # поиск по имени проекта

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'owner', 'created_at')
    list_filter = ('project', 'status', 'owner')  # фильтры
    search_fields = ('title', 'description')  # поиск по названию и описанию
