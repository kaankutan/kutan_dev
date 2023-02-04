from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView, DetailView

from blog.models import Post, Slider, Menu, Page, Social, Category
from blog.forms import CommentForm

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 30

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')

        search_query = self.request.GET.get('query')

        if search_query and self.request.path == '/search/':
            queryset = queryset.filter(Q(title__contains=search_query) | Q(content__contains=search_query))
        
        category = self.kwargs.get('category')

        if category:
            category_obj = get_object_or_404(Category, slug=category)
            queryset = queryset.filter(categories__in=[category_obj])
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['menus'] = Menu.objects.all()

        context['pages'] = Page.objects.all()

        context['socials'] = Social.objects.all()

        if context['page_obj'].number == 1 and self.request.path == '/':
            context['sliders'] = Slider.objects.all()

        search_query = self.request.GET.get('query')
        if search_query:
            context['title'] = f'Search: {search_query}'

        category = self.kwargs.get('category')
        if category:
            context['title'] = f'Category: {category.title()}'
        
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['menus'] = Menu.objects.all()

        context['pages'] = Page.objects.all()

        context['socials'] = Social.objects.all()
        
        context['title'] = context['object'].title
        
        context['commentform'] = CommentForm()

        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'content.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['menus'] = Menu.objects.all()

        context['pages'] = Page.objects.all()

        context['socials'] = Social.objects.all()
        
        context['title'] = context['object'].title
        
        context['commentform'] = CommentForm()

        return context


def create_comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def robots_view(request):
    return render(request, 'robots.txt', content_type='text/plain')
