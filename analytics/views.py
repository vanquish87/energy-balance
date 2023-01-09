from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from weight.models import Weight
import pandas as pd
from datetime import datetime


@login_required(login_url='login')
def dashboard(request):
    '''this is the home'''
    weights = Weight.objects.filter(user=request.user).order_by('date')
    df = pd.DataFrame.from_records(weights.values())

    df['weight'] = df['weight'].fillna(df['weight'].rolling(7).mean().round(2).shift(1))
    df['weight'] = df['weight'].bfill()

    df['7day_MA'] = df['weight'].rolling(7).mean().round(2)

    dates = df['date'][6:].apply(lambda x: x.strftime("%d-%b-%Y")).tolist()
    seven_day_ma = df['7day_MA'][6:].tolist()

    context = {
        'df': df,
        'seven_day_ma': seven_day_ma,
        'dates': dates,
        }
    return render(request, 'analytics/dashboard.html', context)
