from django.contrib import admin
from .models import TopStudents, Post

@admin.register(TopStudents)
class TopStudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass