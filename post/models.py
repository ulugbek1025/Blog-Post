from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField('Title', max_length=50)
    content=RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaratilgan vaqti")
    post_image = models.FileField(blank = True,null = True,verbose_name="Rasm")
    slug = models.SlugField(unique=True, max_length=100)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name='Posts',related_name='comments')
    comment_author = models.CharField(max_length = 50,verbose_name = "Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "content")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']