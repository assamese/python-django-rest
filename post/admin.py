from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ['title']

admin.site.register(Post, PostAdmin)
