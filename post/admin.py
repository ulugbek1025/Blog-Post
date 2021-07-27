from django.contrib import admin
from django.db import models
from post.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','created_date',)
    list_display_links=('title','created_date',)
    search_fields=('title',)
    list_filter=('created_date',)
    prepopulated_fields={'slug':('title',)}

    class Meta:
        model=Post
