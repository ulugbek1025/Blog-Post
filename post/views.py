from django.shortcuts import render
from .models import Post
# Create your views here.


def post(request):
    keyword=request.Get.get('keyword')

    if keyword:
        post=Post.objects.filter(title_contains=keyword)
        return render(request,'post.html',{'post':post})
    post=Post.objects.all()
    return render(request,'post.html',{'post':post})


def index(request):
    return render(request,'index.html')