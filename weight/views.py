from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def create_entry(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            weight = form.save(commit=False)
            weight.owner = request.user
            weight.save()

            return redirect('profile')
    context = {'form': form}
    return render(request, 'weight/create-entry.html', context)