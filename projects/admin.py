from django.contrib import admin
from .models import Project, Blog, Comment, Career

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'description', 'author')
    list_filter = ('created_at', 'author')

# Admin for Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'author')
    list_filter = ('created_at', 'author')

# Admin for Comments on Blogs
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'created_at')
    search_fields = ('author', 'content')
    list_filter = ('created_at', 'author')

# Admin for Career
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

