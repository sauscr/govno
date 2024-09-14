# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import TableOne, TableTwo, TableThree, InitialData
from .forms import TableOneForm, TableTwoForm, InitialDataForm
from .services.base import DataServis


def data_view(request):

    if request.method == 'POST':
        form = InitialDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = InitialDataForm()

    indicators = InitialData.objects.all()

    return render(request,'reports/initial_data.html',
                  {'form': form,
                   'indicators': indicators})




def view_table_one(request):
    # Получаем все данные InitialData
    initial_data_list = InitialData.objects.all()
    table_data = TableOne.objects.all()

    if request.method == 'POST':
        form = TableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TableOneForm()

    # Создаем список для передачи всех данных InitialData в шаблон
    initial_data_values = []
    for initial_data in initial_data_list:
        initial_data_values.append({
            'indicator_name': initial_data.indicator_name,
            'unit': initial_data.unit,
            'plan_value': initial_data.plan_value,
        })

    return render(request, 'reports/tableone.html', {
        'form': form,
        'initial_data_values': initial_data_values,
        'table_data': table_data,
    })


def view_table_two(request):
    if request.method == 'POST':
        form = TableTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TableTwoForm()

    indicators = TableTwo.objects.all()

    return render(request, 'reports/tabletwo.html',
                  {'form': form,
                   'indicators': indicators})