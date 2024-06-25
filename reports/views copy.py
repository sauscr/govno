# reports/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TargetIndicator, Activity, Report, FinancialReport, ActivityReport
from .forms import TargetIndicatorForm, ActivityForm, ReportForm, FinancialReportForm, ActivityReportForm

def index(request):
    return render(request, 'reports/index.html')

def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'reports/activity_list.html', {'activities': activities})

def activity_new(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm()
    return render(request, 'reports/activity_edit.html', {'form': form})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk = pk)
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_list', pk = activity.pk)
    else:
        form = ActivityForm()
    return render(request, 'reports/activity_detail.html', {'form': form, 'activity': activity})

def target_indicator_list(request):
    indicators = TargetIndicator.objects.all()
    return render(request, 'reports/target_indicator_list.html', {'indicators': indicators})

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
    return render(request, 'reports/target_indicator_edit.html', {'form': form})

def target_indicator_edit(request, pk):
    indicator = get_object_or_404(TargetIndicator, pk=pk)
    if request.method == "POST":
        form = TargetIndicatorForm(request.POST, instance=indicator)
        if form.is_valid():
            indicator = form.save()
            return redirect('target_indicator_detail', pk=indicator.pk)
    else:
        form = TargetIndicatorForm(instance=indicator)
    return render(request, 'reports/target_indicator_edit.html', {'form': form})

def target_indicator_new(request):
    if request.method == "POST":
        form = TargetIndicatorForm(request.POST)
        if form.is_valid():
            indicator = form.save()
            return redirect('target_indicator_detail', pk=indicator.pk)
    else:
        form = TargetIndicatorForm()
    return render(request, 'reports/target_indicator_edit.html', {'form': form})

# Similar views can be created for Activity, Report, FinancialReport, and ActivityReport
