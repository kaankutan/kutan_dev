from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Content, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        abstract=True


class Post(Content):
    categories = models.ManyToManyField(Category)


class Page(Content): pass


class Menu(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='childrens', null=True, blank=True)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Slider(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    order = models.IntegerField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=64)
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class Social(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
