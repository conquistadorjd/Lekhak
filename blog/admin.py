from django.contrib import admin
from .models import Post, PostMeta, Comment, CommentMeta, Tag, Category, BlogMeta
# Register your models here.

admin.site.register(Post)
admin.site.register(PostMeta)

admin.site.register(Comment)
admin.site.register(CommentMeta)

admin.site.register(Tag)
admin.site.register(Category)

class BlogMetaAdmin(admin.ModelAdmin):
    list_display = ('meta_key', 'meta_value')
    list_filter = ('meta_key', 'meta_value')
    search_fields = ('meta_key', 'meta_value')
    list_display_links = ('meta_key',)
    list_editable=( 'meta_value',)

admin.site.register(BlogMeta,BlogMetaAdmin)