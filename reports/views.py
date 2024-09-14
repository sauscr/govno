
from django.shortcuts import render, redirect
from .models import TableOne, TableTwo, TableThree, InitialData
from .forms import TableOneForm, TableTwoForm, InitialDataForm



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

    initial_data_list = InitialData.objects.all()
    table_data = TableOne.objects.all()

    if request.method == 'POST':
        form = TableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TableOneForm()

    # Создаем список объединённых данных с использованием zip
    # Список initial_data_values создается только для отображения необходимых полей
    initial_data_values = []
    for initial_data in initial_data_list:
        initial_data_values.append({
            'indicator_name': initial_data.indicator_name,
            'unit': initial_data.unit,
            'plan_value': initial_data.plan_value,
        })

    combined_data = zip(initial_data_values, table_data)

    return render(request, 'reports/tableone.html', {
        'form': form,
        'combined_data': combined_data,
    })


def view_table_two(request):

    initial_data_list = InitialData.objects.all()
    table_data = TableTwo.objects.all()

    if request.method == 'POST':
        form = TableTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TableTwoForm()


    initial_data_values = []
    for initial_data in initial_data_list:
        initial_data_values.append({
            'event_name': initial_data.event_name,
            'rf_set': initial_data.rf_set,
            'mb_set': initial_data.mb_set,
            'vnb_set': initial_data.vnb_set,
        })

    combined_data = zip(initial_data_values, table_data)

    return render(request, 'reports/tableone.html', {
        'form': form,
        'combined_data': combined_data,
    })