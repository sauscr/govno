# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import TargetIndicator, Activity, Report, FinancialReport, ActivityReport
from .forms import TargetIndicatorForm, ActivityForm, ReportForm, FinancialReportForm, ActivityReportForm

def index(request):
    return render(request, 'reports/index.html')

def activity_list(request):
    request.activitys = Activity.objects.all()
    return render(request, 'reports/activity_list.html', {'activities': request.activitys})

def activity_detail(request, pk):    
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'reports/activity_detail.html', {'activity': activity})

def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm()
    return render(request, 'reports/activity_edit.html', {'form': form, 'is_edit': False})

def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk = pk)
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk = activity.pk)
    else:
        form = ActivityForm(request.GET)
    return render(request, 'reports/activity_edit.html', {'form': form, 'is_edit': True})

def target_indicator_list(request):
    request.targetindicators = TargetIndicator.objects.all()
    return render(request, 'reports/target_indicator_list.html', {'indicators': request.targetindicators})

def target_indicator_detail(request, pk):
    indicator = get_object_or_404(TargetIndicator, pk=pk)
    return render(request, 'reports/target_indicator_detail.html', {'indicator': indicator})

def target_indicator_new(request):
    if request.method == "POST":
        form = TargetIndicatorForm(request.POST)
        if form.is_valid():
            indicator = form.save()
            return redirect('target_indicator_detail', pk=indicator.pk)
    else:
        form = TargetIndicatorForm()
    return render(request, 'reports/target_indicator_edit.html', {'form': form, 'is_edit': False})

def target_indicator_edit(request, pk):
    indicator = get_object_or_404(TargetIndicator, pk=pk)
    if request.method == "POST":
        form = TargetIndicatorForm(request.POST, instance=indicator)
        if form.is_valid():
            indicator = form.save()
            return redirect('target_indicator_detail', pk=indicator.pk)
    else:
        form = TargetIndicatorForm(instance=indicator)
    return render(request, 'reports/target_indicator_edit.html', {'form': form, 'is_edit': True})

# Similar views can be created for Activity, Report, FinancialReport, and ActivityReport
