from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from .models import (
    Blog,
    Category,
    Tag
)
# Create your views here.

def home(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    context = {
        'blogs': blogs,
        'tags': tags,
    }
    return render(request, 'home.html', context)

def blogs(request):
    queryset = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')

    context = {
        'blogs': blogs,
        'tags': tags,
        'paginator': paginator
    } 
    return render(request, 'blogs.html', context)

def category_blogs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    blogs = category.category_blogs.all()
    tags = Tag.objects.order_by('-create_date')[:5]
    context = {
        'blogs': blogs,
        'tags': tags
    }

    return render(request, 'category_blogs.html', context)
    
