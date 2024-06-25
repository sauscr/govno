from django.db import models
from django.db.models import JSONField

class TargetIndicator(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    planned_value_per_year = JSONField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=255)
    responsible = models.CharField(max_length=255)
    planned_budget = models.DecimalField(max_digits=10, decimal_places=2)
    expected_result = models.CharField(max_length=255)
    planned_deadline = models.DateField()

    def __str__(self):
        return self.name

class Report(models.Model):
    indicator = models.ForeignKey(TargetIndicator, on_delete=models.CASCADE)
    actual_value = models.DecimalField(max_digits=10, decimal_places=2)
    deviation_reason = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Report for {self.indicator.name}"

class FinancialReport(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    actual_budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    budget_utilization = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Financial Report for {self.activity.name}"

class ActivityReport(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    actual_deadline = models.DateField()
    achieved_result = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Activity Report for {self.activity.name}"
