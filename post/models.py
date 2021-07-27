from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField('Title', max_length=50)
    content=RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaratilgan vaqti")
    article_image = models.FileField(blank = True,null = True,verbose_name="Rasm")
    slug = models.SlugField(unique=True, max_length=100)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']