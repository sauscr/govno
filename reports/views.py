# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import TableOne, TableTwo
from .forms import TableOneForm, TableTwoForm

def view_table_one(request):
    """
    View-функция для отображения и добавления данных первой таблицы.
    """
    
    
    if request.method == 'POST':
        form = TableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicator_one')

    else:
        form = TableOneForm()
    
    indicators = TableOne.objects.all()

    return render(request,'reports/tableone.html',
                  {'form': form,
                   'indicators': indicators})

    indicators = TableOne.objects.all()

    context = {
        'form': TableOneForm(),
        'indicators': indicators
    }

    return render(request, 'reports/tableone.html', context)

def edit_tableone(request, id):
    """
    Функция для редактирования данных индикатора.
    """
    indicator = get_object_or_404(TableOne, id=id)
    if request.method == 'POST':
        form = TableOneForm(request.POST, instance=indicator)
        if form.is_valid():
            form.save()
            return redirect('indicator_one')
    else:
        form = TableOneForm(instance=indicator)
    
    return render(request, 'reports/tableone.html', {'form': form})

def delete_tableone(request, id):
    """
    Функция для удаления индикатора.
    """
    indicator = get_object_or_404(TableOne, id=id)
    indicator.delete()
    return redirect('indicator_one')



def view_table_two(request):

    context = 'Крутое название сайта'

    if request.method == 'POST':
        form = TableTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicator_two')
    else:
        form = TableTwoForm()

    indicators = TableTwo.objects.all()

    return render(request, 'reports/tabletwo.html',
                  {'form': form,
                   'indicators': indicators,
                   })