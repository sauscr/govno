
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
            instance = form.save(commit=False)
            instance.result = instance.result
            instance.percentage_deviation = instance.percentage_deviation
            instance.save()
            return redirect('')
    else:
        form = TableOneForm()

    initial_data_values = []
    for initial_data in initial_data_list:
        initial_data_values.append({
            'indicator_name': initial_data.indicator_name,
            'unit': initial_data.unit,
            'plan_value': initial_data.plan_value,
        })

    table_data_values = []
    for table_item in table_data:
        table_data_values.append({
            'actual_value': table_item.actual_value,
            'result': table_item.result,
            'percentage_deviation': table_item.percentage_deviation,
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
            instance = form.save(commit=False)
            instance.planned_sum_set = instance.planned_sum_set
            instance.actual_sum = instance.actual_sum
            instance.planned_sum = instance.planned_sum
            instance.save()
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

    table_data_values = []
    for table_item in table_data:
        table_data_values.append({
            'rf_actually': table_item.rf_actually,
            'mb_actually': table_item.mb_actually,
            'vnb_actually': table_item.vnb_actually,
            'plannedplanned_sum_set_sum': table_item.planned_sum_set,
            'actual_sum': table_item.actual_sum,
            'planned_sum': table_item.planned_sum,
        })
    
    combined_data = zip(initial_data_values, table_data)

    return render(request, 'reports/tableone.html', {
        'form': form,
        'combined_data': combined_data,
    })