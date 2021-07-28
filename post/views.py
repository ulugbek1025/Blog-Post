from django.core.checks import messages
from post.forms import PostForm
from django.shortcuts import redirect, render,get_object_or_404,reverse
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.contrib import messages
# Create your views here.


def post(request):
    keyword=request.GET.get('keyword')

    if keyword:
        post=Post.objects.filter(title=keyword)
        return render(request,'post.html',{'post':post})
    post=Post.objects.all()
    return render(request,'post.html',{'post':post})


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



@login_required(login_url='user:login')
def dashboard(request):
    posts=Post.objects.filter(author=request.user)
    return render (request,'dashboard.html',{'posts':posts})


@login_required(login_url='user:login')
def addPost(request):
    form=PostForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        post=form.save(commit=False)
        post.slug=slugify(post.title)
        post.author=request.user
        post.save()
        messages.success(request,'Post created successfully')
        return redirect('post:dashboard')
    return render(request,'addpost.html',{'form':form})


@login_required(login_url='user:login')
def detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    comments=post.comments.all()
    context={
        'post':post,
        'comments':comments
    }
    return render(request,'detail.html',context)


@login_required(login_url='user:login')
def update(request,slug):

    post=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        post=form.save(commit=False)

        post.author=request.user
        post.save()

        messages.success(request,'Update')
        return redirect('post:dashboard')
    
    return render(request,'update.html',{'form':form})


@login_required(login_url='user:login')
def delete(request,slug):
    post=get_object_or_404(Post,slug=slug)

    post.delete()
    messages.success(request,'delete post')
    return redirect('post:dashboard')


def addCommit(request,slug):
    post=get_object_or_404(Post,slug=slug)

    if request.method=='POST':
        comment_author=request.POST.get('comment_author')
        comment_content=request.POST.get('comment_content')

        new_comment=Comment(comment_author=comment_author,comment_content=comment_content)
        new_comment.post=post
        new_comment.save()
    return redirect(reverse('post:detail',kwargs={'slug':slug}))