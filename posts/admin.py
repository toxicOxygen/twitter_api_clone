from django.contrib import admin
from .models import Post,PostImage

# Register your models here.
class PostImagesInline(admin.TabularInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','tweet','created','update']
    inlines = [PostImagesInline,]
