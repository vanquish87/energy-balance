from django.shortcuts import render


def profile(request):
    context = {}
    return render(request, 'account/profile.html', context)
