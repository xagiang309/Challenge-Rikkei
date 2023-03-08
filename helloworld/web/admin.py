from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date_posted' ]
    list_filter = ['date_posted']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)