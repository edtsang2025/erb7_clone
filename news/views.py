from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, Paginator

# Create your views here.

from news.models import Article

def news(request):


    news = Article.objects.filter(is_published=True)

    paginator = Paginator(news,5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {"news":paged_listings,}
    
        
    return render(request, 'news/news.html', context)

def article(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    context = {"article":article,}
    
    return render(request, 'news/article.html', context)


