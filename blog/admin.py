from django.contrib import admin
from .models import MyBlog

# Registering models here....
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp', 'updated']
    list_filter = ['updated']


admin.site.register(MyBlog, BlogAdmin)
