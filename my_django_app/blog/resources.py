
from import_export import resources
from blog.models import Blog

class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'author', 'text', 'create_at')
