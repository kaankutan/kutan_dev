"""kutan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from django.urls import path, include

from blog.views import PostListView, PostDetailView, PageDetailView, create_comment_view, robots_view
from blog.sitemaps import PostSitemap, CategorySitemap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view()),
    path('post/<str:slug>/', PostDetailView.as_view()),
    path('page/<str:slug>/', PageDetailView.as_view()),
    path('summernote/', include('django_summernote.urls')),
    path('create-comment/', create_comment_view),
    path('category/<str:category>/', PostListView.as_view()),
    path('search/', PostListView.as_view()),
    path('sitemap.xml/', sitemap, {'sitemaps': {'posts': PostSitemap, 'categories': CategorySitemap}}),
    path('robots.txt/', robots_view),
]


admin.site.site_header = 'Kutan BLOG'