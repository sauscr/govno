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
                                   )

    @property
    def relative_deviation(self):
        return CalculationServices.\
            Math.calculate_relative_diviation(
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
    name = models.CharField(max_length=255,
                            verbose_name='Наименование мероприятия',
                            default='')
    # Планируемые значения
    rf_set = models.FloatField(verbose_name='Референс',)
    mb_set = models.FloatField(verbose_name='МБ',)
    vnb_set = models.FloatField(verbose_name='ВНБ',)

    # Реальные значения
    rf_actually = models.FloatField(verbose_name='Референс',)
    mb_actually = models.FloatField(verbose_name='МБ',)
    vnb_actually = models.FloatField(verbose_name='ВНБ',)


    @property
    def planned_sum(self):
        return CalculationServices.calculate_sums(
            self.rf_set, self.mb_set, self.vnb_set)

    @property
    def actual_sum(self):
        return CalculationServices.calculate_sums(
            self.rf_actually, self.mb_actually, self.vnb_actually)
    

    @property
    def mastered_to_unmastered(self):
        return CalculationServices.Math.\
            calculate_ratio_mastered_to_unmastered(
            self.actual_sum, self.planned_sum)

    def __str__(self):
        return self.name