from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = 'Categories'


STATUS_CHOICES = (
    ("Draft","Draft"),
    ("Published","Published")
)
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_desc = models.TextField()
    blog_body = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment



