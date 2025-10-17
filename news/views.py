from django.shortcuts import render

# Create your views here.

def news(request):
    return render(request, 'news/news.html')

def article(request):
    return render(request, 'news/article.html')