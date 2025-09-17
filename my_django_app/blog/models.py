from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name='სათაური', max_length=100)
    text = models.TextField(verbose_name='ტექსტი')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title
