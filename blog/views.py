from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})  # render 장고가 지원하는 템플릿 시스템
