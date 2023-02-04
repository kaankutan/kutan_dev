from django.contrib.sitemaps import Sitemap
from blog.models import Post, Category


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = "1"
    
    def items(self):
        # Return a list of objects that should be included in the sitemap.
        # You can retrieve this list of objects from the database or generate it dynamically.
        return Post.objects.all()

    def location(self, obj):
        # Return the URL for a given object.
        return '/post/{}/'.format(obj.slug)


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = "1"

    def items(self):
        # Return a list of objects that should be included in the sitemap.
        # You can retrieve this list of objects from the database or generate it dynamically.
        return Category.objects.all()

    def location(self, obj):
        # Return the URL for a given object.
        return '/category/{}/'.format(obj.slug)