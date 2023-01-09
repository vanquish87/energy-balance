from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WeightForm
from django.contrib import messages
import csv
from .models import Weight
import codecs
from datetime import datetime


# Create your views here.
@login_required(login_url='login')
def create_entry(request):
    form = WeightForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(request.POST)
            try:
                weight = Weight.objects.get(date=request.POST['date'], user=request.user)
                weight.calorie_intake = request.POST['calorie_intake']
                weight.weight = request.POST['weight']
                print(weight)
            except:
                weight = form.save(commit=False)
                weight.user = request.user

            weight.save()
            messages.success(request, 'New weight entry successful!')
            return redirect('profile')

        messages.warning(request, 'Form is filled incorrectly.')

    context = {'form': form}
    return render(request, 'weight/create-entry.html', context)


@login_required(login_url='login')
def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        data = []
        reader = csv.DictReader(codecs.iterdecode(csv_file, 'utf-8'))
        for row in reader:
            data.append(row)
        for row in data:
            date = datetime.strptime(row['Date'], '%d/%m/%Y')
            formatted_date = date.strftime('%Y-%m-%d')
            try:
                weight = Weight.objects.get(date=formatted_date, user=request.user)
            except:
                weight = Weight()

            weight.date = formatted_date

            if row['Weight']:
                weight.weight = row['Weight']
            if row['IN']:
                weight.calorie_intake = row['IN']
            # print(row['Date'], row['Weight'], row['IN'])
            weight.user = request.user
            weight.save()

        messages.success(request, 'CSV imported successfully!')
        return redirect('index')
    return render(request, 'weight/import-csv.html')