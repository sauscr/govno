# from django.conf import settings
from django.db import models
from django.db.models import JSONField

from .services.logic import CalculationServices

class TableOne(models.Model):

    name = models.CharField(max_length=255,
                            verbose_name=
                            'Наименование целевого индикатора и показателя',)
    plan_value = models.FloatField(verbose_name=
                                   'План на текущий год',)
    actual_value = models.FloatField(verbose_name=
                                     'Значение на конец отчетного периода',)
    diff_reason = models.CharField(max_length=255,
                                   verbose_name=
                                   'Обоснование отклонения фактического значения',
                                   default='')

    @property
    def relative_deviation(self):
        return CalculationServices.calculate_relative_diviation(
            self.plan_value,
            self.actual_value,
            )

    @property
    def result_end(self):
        return CalculationServices.result(
            self.plan_value,
            self.actual_value,
            )


    def __str__(self):
        return self.name
    


class TableTwo(models.Model):
    pass