from django.shortcuts import get_object_or_404,redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html', {
        'post_list': qs,  # post_list html 부분
    })  # render 장고가 지원하는 템플릿 시스템

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # pk = '100"
#   try:
#        post = Post.objects.get(pk=pk)
#    except Post.DoesNotExist:
#       raise Http404 #Page Not Found from django.http import Http404
    return render(request, 'blog/post_detail.html', {'post': post, })

def post_new(request):
    # request.POST, request.FILES
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form, })
