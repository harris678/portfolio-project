from django.shortcuts import render
from .models import Blog
def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blogs = Blog.objects.filter(id=blog_id)
    blogs = blogs.first()
    return render(request,'blog/detail.html',{'blogs':blogs})
