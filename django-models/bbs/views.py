from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect

from .models import Article, Title

User = get_user_model()


def article_list(request):
    latest_article_list = get_list_or_404(
        Article.objects.order_by('created_date')
    )
    context = {
        'latest_article_list': latest_article_list,
        'title': Title.objects.first(),
    }
    return render(request, 'bbs/article_list.html', context = context)


def article_detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article': article,
        'pk': pk
    }
    return render(request, 'bbs/article_detail.html', context)


def article_add(request):
    if request.method == 'GET':
        user = get_user_model()
        context = {
            'article': Article(),
        }
        return render(request, 'bbs/article_add.html', context)

    elif request.method == 'POST':
        data = request.POST
        # user = User()
        print(data)
        # print('user id:', user)
        article = Article.objects.create(
            # author = 1,
            title_id = 1,
            subtitle = data['subtitle'],
            description1 = data['description1'],
            examples = data['examples'],
            description2 = data['description2'],
        )
        article.save()
        return redirect('bbs:article_detail', pk = article.pk)


def article_markdown(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'bbs/article_markdown.html', context)


def article_modify(request, pk):
    article = Article.objects.get(pk = pk)
    if request.method == 'GET':
        context = {
            'article': article,
            'pk':pk
        }
        return render(request, 'bbs/article_modify.html', context)
    elif request.method == 'POST':
        data = request.POST
        article.subtitle = data['subtitle']
        article.description1 = data['description1']
        article.examples = data['examples']
        article.description2 = data['description2']
        article.save()
        return redirect('bbs:article_detail', pk = article.pk)


def article_delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk = pk)
        article.delete()
        return redirect('bbs:list')
    else:
        return HttpResponse('Method "GET" is not allowed.')

