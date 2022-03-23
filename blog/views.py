from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostMeta, Comment, CommentMeta, Tag, Category
from .forms import CommentForm

def index(request):
    print("*** Inside index",)
    # context = Post.objects.filter(post_status='published',post_group__exact="")
    context = Post.objects.filter(post_status='published').order_by('-post_date')
    tags = Tag.objects.all()
    print("*** context", context)
    return render(request, 'blog/index.html',{'context':context, 'tags':tags})  


def detail(request, post_slug):
    # blog_post = Post.objects.get(post_slug=post_slug)
    blog_post = get_object_or_404(Post, post_slug=post_slug)
    print("*** === post_slug : ", post_slug)
    # comments = get_object_or_404(Comment,comment_post_id=blog_post.post_id) # works only for one value
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
    return render(request, 'blog/aboutus.html')  

def contactus(request):
    return render(request, 'blog/contactus.html')       