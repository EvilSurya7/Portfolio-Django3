from django.shortcuts import render, get_object_or_404
from .models import Blogs


# Create your views here.

def blog(request):
    blogs = Blogs.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs':blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', { 'blog':blog })
