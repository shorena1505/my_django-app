from django.contrib import admin
from blog.models import Blog, BlogImage, Author


admin.site.register(Blog)
admin.site.register(BlogImage)
admin.site.register(Author)

