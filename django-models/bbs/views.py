from django.shortcuts import render


def article_list(request):
    context = {

    }
    return render(request, 'list', context = context)
