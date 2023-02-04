from django.contrib import admin
from blog.models import Post, Page, Category, Menu, Slider, Social
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)

class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Page, PageAdmin)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Slider)
admin.site.register(Social)
