#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse,Http404

from .models import *
from .forms import CommentForm

def home(request):
    return render(request,"blog/blog_index.html",{})

def get_blogs(request):
    """获取博客内容"""
    blogs=Blog.objects.all().order_by('-pub')#获得所有的博客按时间排序
    return render(request,'blog/blog_list.html',{'blogs':blogs})


def get_details(request,blog_id):
    """获取博客明细"""
    try:
        blog=Blog.objects.get(id=blog_id)#获取固定的blog_id的对象；
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:#请求方法为Post
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data=form.cleaned_data
            cleaned_data['blog']=blog
            Comment.objects.create(**cleaned_data)
    res={
        'blog':blog,
        'comments': blog.comment_set.all().order_by('-pub'),
        'form': form
    }
    return render(request,'blog/blog_details.html',res)