# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
<<<<<<< HEAD
from .models import TableOne
from .forms import TargetIndicatorForm
from .csrf import csrf_exempt

@csrf_exempt
def target_indicator_view(request, pk = None):
    if request.method == 'POST':
        
        form = TargetIndicatorForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('target_indicator')  # Перенаправление на страницу успеха после сохранения
        else:
            print("Форма невалидна", form.errors)
=======
from .models import TableOne, TableTwo
from .forms import TableOneForm, TableTwoForm

def view_table_one(request):
    
    if request.method == 'POST':
        form = TableOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('target_indicator')
>>>>>>> 39e8d485cd2b440bd5b7c1baf0bb86e0c64a7ef9
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