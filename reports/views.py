
from django.shortcuts import render, redirect
from .models import TableOne, TableTwo, TableThree, InitialData
from .forms import TableOneForm, TableTwoForm, InitialDataForm


def process_form(request, form_class, redirect_url):
    '''
    Обработчик формы
    '''
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            isinstance = form.save(commit=False)
            isinstance.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return form


def get_initial_values(initial_data_list, fields):
    '''
    Возвращает данные изInitialData в виде списка словарей
    '''
    return [
        {field: getattr(initial_data, field) for field in fields}
        for initial_data in initial_data_list
    ]


def get_table_data_values(table_data, fields):
    '''
    Возвращает данные из TableData в виде списка словарей
    '''
    return [
        {field: getattr(table_data, field) for field in fields}
        for table_data in table_data
    ]






def data_view(request):
    url = '/reports/tableone/'
    form = process_form(request, InitialDataForm, url)
    values = InitialData.objects.all()

    return render(request,'reports/initial_data.html',{
        'form': form,
        'values': values,
    })


def view_table_one(request):
    url = '/reports/tableone/'
    form = process_form(request, TableOneForm, url)

    initial_data_walues = get_initial_values(
        InitialData.objects.all(),
        ['indicator_name', 'unit', 'plan_value',]
    )

    table_data_values = get_table_data_values(
        TableOne.objects.all(),
        ['actual_value', 'result', 'percentage_deviation',]
    )

    combined_data = zip(initial_data_walues, table_data_values)

    return render(request, 'reports/tableone.html',{
        'form': form,
        'combined_data': combined_data,
    })


def view_table_two(request):
    url = '/reports/tabletwo/'
    form = process_form(request, TableTwoForm, url)

    initial_data_walues = get_initial_values(
        InitialData.objects.all(),
        ['event_name', 'rf_set', 'rb_set', 'mb_set', 'vnb_set',]
    )

    table_data_values = get_table_data_values(
        TableTwo.objects.all(),
        ['rf_actually', 'mb_actually', 'vnb_actually',
         'planned_sum', 'actual_sum', 'percent',]
    )
    combined_data = zip(initial_data_walues, table_data_values)

    return render(request,'reports/tabletwo.html', {
        'form': form,
        'combined_data': combined_data,
    })


def view_table_three(request):
    pass