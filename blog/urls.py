from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap   #added for sitemap
from .sitemaps import PostSitemap                   #added for sitemap

sitemaps = {
    'posts': PostSitemap
}


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),  
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps } , name='sitemap'), 
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),  
    path('<post_slug>/', views.detail, name='detail'),
    path('tag/<tag_slug>/',views.post_tag, name='post_tag'),
   
    
]