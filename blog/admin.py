from django.contrib import admin
from .models import Post, PostMeta, Comment, CommentMeta, Tag, Category
# Register your models here.

admin.site.register(Post)
admin.site.register(PostMeta)

admin.site.register(Comment)
admin.site.register(CommentMeta)

admin.site.register(Tag)
admin.site.register(Category)
