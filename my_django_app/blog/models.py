from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name='სათაური', max_length=100)
    text = models.TextField(verbose_name='ტექსტი')
    is_active = models.BooleanField(verbose_name='აქტიურია', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    authors = models.ManyToManyField(to="Author",related_query_name ="blog", verbose_name="ავტორი")
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['title']



    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='Blog Post', on_delete=models.CASCADE)

    image = models.ImageField(verbose_name="Image", upload_to='blog_images/')

    class Meta:
        verbose_name = "Blog Image"
        verbose_name_plural = "Blog Images"

    def __str__(self):
        return f"{self.blog.title} - {self.blog.title}"


class Author(models.Model):
    first_name=models.CharField(verbose_name='სახელი',max_length=100)
    last_name=models.CharField(verbose_name='გვარი',max_length=100)
    email=models.CharField(verbose_name='იმეილი')

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



