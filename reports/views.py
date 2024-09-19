
from django.shortcuts import render, redirect
from services.view_services import *
from .models import TableOne, TableTwo, TableThree, InitialData
from .forms import TableOneForm, TableTwoForm, TableThreeForm, InitialDataForm

def process_form(request, form_class, redirect_url):
    '''
    Обработчик формы
    '''
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance .save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return form






def data_view(request):
    url = '/reports/tableone/'
    form = process_form(request, InitialDataForm, url)
    values = get_all_objects(InitialData)

    return render(request, 'reports/initial_data.html', {
        'form': form,
        'values': values,
    })


def view_table_one(request):
    url = '/reports/tableone/'
    form = process_form(request, TableOneForm, url)

    initial_data_values = get_values(
        get_all_objects(InitialData),
        ['indicator_name', 'unit', 'plan_value',]
    )

    table_data_values = get_values(
        get_all_objects(TableOne),
        ['actual_value', 'result', 'percentage_deviation',]
    )

    combined_data = zip(initial_data_values, table_data_values)

    return render(request, 'reports/tableone.html', {
        'form': form,
        'combined_data': combined_data,
    })


def view_table_two(request):
    url = '/reports/tabletwo/'
    form = process_form(request, TableTwoForm, url)

    initial_data_values = get_values(
        get_all_objects(InitialData),
        ['event_name', 'rf_set', 'rb_set', 'mb_set', 'vnb_set',]
    )

    table_data_values = get_values(
        get_all_objects(TableTwo),
        ['rf_actually', 'rb_actually', 'mb_actually', 'vnb_actually',
         'planned_sum', 'actual_sum', 'percent',]
    )

    combined_data = zip(initial_data_values, table_data_values)

    return render(request, 'reports/tabletwo.html', {
        'form': form,
        'combined_data': combined_data,
    })


def view_table_three(request):
    url = '/reports/tablethree/'
    form = process_form(request, TableThreeForm, url)

    initial_data_values = get_values(
        get_all_objects(InitialData),
        ['event_name', 'expected_result', 'time_execution_plan',]
    )

    table_data_values = get_values(
        get_all_objects(TableThree),
        ['actual_result', 'time_execution_actually',
         'executor', 'result', 'percent',]
    )

    combined_data = zip(initial_data_values, table_data_values)

    return render(request, 'reports/tablethree.html', {
        'form': form,
        'combined_data': combined_data,
    })
