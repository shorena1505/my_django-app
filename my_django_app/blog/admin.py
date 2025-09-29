from django.contrib import admin
from blog.models import Blog, BlogImage, Author


admin.site.register(BlogImage)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'create_at')
    list_filter = ('is_active','authors')
    search_fields = ('title',)
    ordering = ('title',)
    date_hierarchy = 'create_at'
    filter_horizontal = ('authors',)
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Blog, BlogAdmin)