from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    '''this is the home'''
    context = {}
    return render(request, 'index/index.html', context)
