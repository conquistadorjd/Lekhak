from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostMeta, Comment, CommentMeta, Tag, Category, BlogMeta
from .forms import CommentForm

def index(request):
    context = Post.objects.filter(post_status='published').order_by('-post_date')
    tags = Tag.objects.all()
    blog_title = get_object_or_404(BlogMeta, meta_key='title').get_meta_value()
    print("*** blog_title : ", blog_title)
    return render(request, 'blog/index.html',{'context':context, 'tags':tags, 'blog_title': blog_title})  


def detail(request, post_slug):
    # blog_post = Post.objects.get(post_slug=post_slug)
    blog_post = get_object_or_404(Post, post_slug=post_slug)
    # print("*** === post_slug : ", post_slug)
    comments = Comment.objects.filter(comment_post_id=blog_post.post_id,comment_status='published')
    # print("*** blog_post.post_id", blog_post.post_id)
    # print("** blog_Post: ", blog_post.post_slug)
    # print("** post_content: ", blog_post.post_content)
    # print("*** comments", comments)
    print("*** post_title", blog_post.post_title)
    # print("*** post_comments", blog_post.post_comments)   # comments column is removed from model
    print("*** post_tags", blog_post.post_tags)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.comment_post_id = blog_post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html', {'blog_post': blog_post,'comments':comments,'new_comment': new_comment,'comment_form': comment_form, })

def post_tag(request, tag_slug):
    tag = get_object_or_404(Tag, tag_slug=tag_slug)
    print("*** tag", tag)
    context = Post.objects.filter(post_tags__in=[tag])
    # context = Post.objects.filter(comment_post_id=blog_post.post_id)
    print("*** context", context)
    tags = Tag.objects.all()
    return render(request, 'blog/index.html',{'context':context, 'tags':tags})  

def aboutus(request):
    aboutus = get_object_or_404(BlogMeta, meta_key='aboutus').get_meta_value()
    return render(request, 'blog/aboutus.html',{'aboutus': aboutus})  

def contactus(request):
    contactus = get_object_or_404(BlogMeta, meta_key='contactus').get_meta_value()
    return render(request, 'blog/contactus.html',{'contactus': contactus})       