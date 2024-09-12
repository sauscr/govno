# reports/forms.py
from django import forms
from .models import TableOne
from django.core.exceptions import ValidationError
import json



class TargetIndicatorForm(forms.ModelForm): # первая таблица
    class Meta:
        model = TableOne
        fields = ['name', 'plan_value', 'actual_value', 'diff_reason',  ]

    def clean(self):
        cleaned_data = super().clean()
        plan_value = cleaned_data.get('plan_value')
        actual_value = cleaned_data.get('actual_value')

        if plan_value is None or actual_value is None:
            raise forms.ValidationError("Плановое и фактическое значения обязательны для заполнения.")
        
        return cleaned_data
    

    

    '''    def clean_unit(self):
        unit = self.cleaned_data.get('unit')
        if not unit:
            raise forms.ValidationError('This field is required.')
        if len(unit) > 50:
            raise forms.ValidationError('Unit is too long.')
        return unit
    
    def clean_planned_value_per_year(self):
        data = self.cleaned_data['plan_value']
        if isinstance(data, int):
            raise ValidationError("Enter a valid JSON string")
        try:
            json_data = json.loads(data)
        except json.JSONDecodeError:
            raise ValidationError('Invalid JSON data')
        return json_data
    



    class ActivityForm(forms.ModelForm):
    planned_deadline = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(format='%d.%m.%Y')
    )
    class Meta:
        model = Activity
        fields = ['name', 'responsible', 'planned_budget', 'expected_result', 'planned_deadline']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required.')
        if len(name) > 255:
            raise forms.ValidationError('Name is too long.')
        return name

    def clean_responsible(self):
        responsible = self.cleaned_data.get('responsible')
        if not responsible:
            raise forms.ValidationError('This field is required.')
        if len(responsible) > 255:
            raise forms.ValidationError('Responsible is too long.')
        return responsible

    def clean_planned_budget(self):
        planned_budget = self.cleaned_data.get('planned_budget')
        if planned_budget <= 0:
            raise forms.ValidationError('Planned budget must be greater than zero.')
        return planned_budget

    def clean_expected_result(self):
        expected_result = self.cleaned_data.get('expected_result')
        if not expected_result:
            raise forms.ValidationError('This field is required.')
        return expected_result

    def clean_planned_deadline(self):
        planned_deadline = self.cleaned_data.get('planned_deadline')
        if not planned_deadline:
            raise forms.ValidationError('This field is required.')
        return planned_deadline




class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['indicator', 'actual_value', 'deviation_reason', 'status']

    def clean_actual_value(self):
        actual_value = self.cleaned_data.get('actual_value')
        if actual_value < 0:
            raise forms.ValidationError('Actual value cannot be negative.')
        return actual_value

class FinancialReportForm(forms.ModelForm):
    class Meta:
        model = FinancialReport
        fields = ['activity', 'actual_budget', 'total_budget', 'budget_utilization']

    def clean_actual_budget(self):
        actual_budget = self.cleaned_data.get('actual_budget')
        if actual_budget < 0:
            raise forms.ValidationError('Actual budget cannot be negative.')
        return actual_budget

    def clean_total_budget(self):
        total_budget = self.cleaned_data.get('total_budget')
        if total_budget <= 0:
            raise forms.ValidationError('Total budget must be greater than zero.')
        return total_budget

    def clean_budget_utilization(self):
        budget_utilization = self.cleaned_data.get('budget_utilization')
        if budget_utilization < 0 or budget_utilization > 100:
            raise forms.ValidationError('Budget utilization must be between 0 and 100.')
        return budget_utilization

class ActivityReportForm(forms.ModelForm):
    class Meta:
        model = ActivityReport
        fields = ['activity', 'actual_deadline', 'achieved_result', 'status', 'completion_percentage']
    
    def clean_actual_deadline(self):
        actual_deadline = self.cleaned_data.get('actual_deadline')
        if not actual_deadline:
            raise forms.ValidationError('This field is required.')
        return actual_deadline

    def clean_achieved_result(self):
        achieved_result = self.cleaned_data.get('achieved_result')
        if not achieved_result:
            raise forms.ValidationError('This field is required.')
        return achieved_result

    def clean_completion_percentage(self):
        completion_percentage = self.cleaned_data.get('completion_percentage')
        if completion_percentage < 0 or completion_percentage > 100:
            raise forms.ValidationError('Completion percentage must be between 0 and 100.')
        return completion_percentage
        '''