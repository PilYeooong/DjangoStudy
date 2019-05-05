from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })  # render 장고가 지원하는 템플릿 시스템
