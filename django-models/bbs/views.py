from django.shortcuts import render, get_list_or_404

from .models import Article


def article_list(request):
    latest_article_list = get_list_or_404(
        Article.objects.all()
    )
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request, 'bbs/article_list.html', context = context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
        'pk': pk
    }
    return render(request, 'bbs/article_detail.html', context)
