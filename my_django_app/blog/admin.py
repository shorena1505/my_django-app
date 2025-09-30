from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from import_export.admin import ImportExportModelAdmin

from blog.models import Blog, BlogImage, Author
from blog.resources import BlogResource


class BlogImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = BlogImage
    extra = 1



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age')


class BlogAdmin(ImportExportModelAdmin, SortableAdminMixin):
    resource_class = BlogResource
    list_display = ('title', 'is_active', 'create_at')
    list_filter = ('is_active','authors')
    search_fields = ('title',)
    ordering = ('order',)
    date_hierarchy = 'create_at'
    filter_horizontal = ('authors',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlogImageInline]




admin.site.register(Blog, BlogAdmin)