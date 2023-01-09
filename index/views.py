from django.shortcuts import render


def index(request):
    '''this is the home'''
    context = {}
    return render(request, 'index/index.html', context)
