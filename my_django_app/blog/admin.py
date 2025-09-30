from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from import_export.admin import ImportExportModelAdmin
from nested_admin.nested import NestedTabularInline, NestedModelAdmin

from blog.models import Blog, BlogImage, Author, BlogImageDescription
from blog.resources import BlogResource

class BlogImageDescriptionInline(NestedTabularInline):
    model = BlogImageDescription
    extra = 1


class BlogImageInline(NestedTabularInline):
    model = BlogImage
    inlines = [BlogImageDescriptionInline]
    extra = 1
    fk_name = 'blog'



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age')


class BlogAdmin(ImportExportModelAdmin, NestedModelAdmin):
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