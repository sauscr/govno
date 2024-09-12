# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import TableOne, TableTwo
from .forms import TableOneForm, TableTwoForm

def view_table_one(request):
    
    if request.method == 'POST':
        form = TableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('target_indicator')
    else:
        form = TableOneForm()
    
    indicators = TableOne.objects.all()

    return render(request,'reports/tableone.html',
                  {'form': form,
                   'indicators': indicators})


def view_table_two(request):
    if request.method == 'POST':
        form = TableTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('target_indicator_two')
    else:
        form = TableTwoForm()

    indicators = TableTwo.objects.all()

    return render(request, 'reports/tabletwo.html',
                  {'form': form,
                   'indicators': indicators})