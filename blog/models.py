from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from django.template.defaultfilters import slugify # new
from ckeditor.fields import RichTextField

STATUS_CHOICES = (
    ('draft','draft'),
    ('submitted','submitted'),
    ('approved', 'approved'),
    ('published','published'),
)
# Create your models here.


class Post(models.Model):
    post_id         = models.AutoField(primary_key=True)
    post_author     = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post_date       = models.DateTimeField(default=timezone.now)
    post_content    = RichTextField()
    post_title      = models.TextField(null=True, blank=True)
    post_excerpt    = models.TextField(null=True, blank=True)
    post_img        = models.ImageField(upload_to='post_images', null=True,blank=True)
    post_status     = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    post_comment_status  = models.CharField(max_length=10,blank=True)
    post_slug       = models.SlugField(max_length=255, null=True, blank=True)    
    post_category   = models.ForeignKey('Category', null=True,blank=True, on_delete=models.PROTECT, related_name='category_set')
    post_tags       = models.ManyToManyField('Tag',blank=True)

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs): # new
        if not self.post_slug:
            self.post_slug = slugify(self.post_title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self): #this is added for sitemap
        return '/'+self.post_slug


class PostMeta(models.Model):
    meta_id         =   models.AutoField(primary_key=True)
    meta_post_id    =   models.ForeignKey(Post, on_delete=models.CASCADE)
    meta_key        =   models.CharField(max_length=255)
    meta_value      =   models.TextField(null=True, blank=True)


class Comment(models.Model):
    comment_id              = models.AutoField(primary_key=True)
    comment_post_id         = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author          = models.CharField(max_length=50)
    comment_author_email    = models.CharField(max_length=100)
    comment_author_IP       = models.CharField(max_length=50)
    comment_date            = models.DateTimeField(default=timezone.now)
    comment_content         = RichTextField()   
    comment_status          = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    comment_parent          = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return f"Comment by {self.comment_author} on {self.comment_post_id}"

class CommentMeta(models.Model):
    meta_id         =   models.AutoField(primary_key=True)
    meta_comment_id =   models.ForeignKey(Comment, on_delete=models.CASCADE)
    meta_key        =   models.CharField(max_length=255)
    meta_value      =   models.TextField(null=True, blank=True)

class Tag(models.Model):
    tag_id         =   models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255, unique=True)
    tag_slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.tag_name

    def save(self, *args, **kwargs): # new
        if not self.tag_slug:
            self.tag_slug = slugify(self.tag_name)
        return super().save(*args, **kwargs)


class Category(models.Model):
    category_id         =   models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, unique=True)
    category_slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs): # new
        if not self.category_slug:
            self.category_slug = slugify(self.category_name)
        return super().save(*args, **kwargs)