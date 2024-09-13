# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import TableOne, TableTwo
from .forms import TableOneForm, TableTwoForm

def view_table_one(request):
    if request.method == 'POST':
        form = TableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicator_one')
    else:
        form = TableOneForm()
    
    indicators = TableOne.objects.all()

    return render(request, 'reports/tableone.html', {'form': form, 'indicators': indicators})

def edit_tableone(request, id):
    indicator = get_object_or_404(TableOne, id=id)
    if request.method == 'POST':
        form = TableOneForm(request.POST, instance=indicator)
        if form.is_valid():
            form.save()
            return redirect('indicator_one')
    else:
        form = TableOneForm(instance=indicator)
    
    if request.is_ajax():
        return render(request, 'reports/partials/edit_tableone_form.html', {'form': form})
    
    return render(request, 'reports/tableone.html', {'form': form})

def delete_tableone(request, id):
    indicator = get_object_or_404(TableOne, id=id)
    indicator.delete()
    return redirect('indicator_one')

def view_table_two(request):
    if request.method == 'POST':
        form = TableTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indicator_two')
    else:
        form = TableTwoForm()
    
    indicators = TableTwo.objects.all()

    return render(request, 'reports/tabletwo.html', {'form': form, 'indicators': indicators})

def edit_tabletwo(request, id):
    indicator = get_object_or_404(TableTwo, id=id)
    if request.method == 'POST':
        form = TableTwoForm(request.POST, instance=indicator)
        if form.is_valid():
            form.save()
            return redirect('indicator_two')
    else:
        form = TableTwoForm(instance=indicator)
    
    # if request.is_ajax():
    #     return render(request, 'reports/edit_tabletwo.html', {'form': form})
    
    return render(request, 'reports/tabletwo.html', {'form': form})

def delete_tabletwo(request, id):
    indicator = get_object_or_404(TableTwo, id=id)
    indicator.delete()
    return redirect('indicator_two')
