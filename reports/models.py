from django.db import models

class TableOne(models.Model):

    actual_value = models.FloatField(verbose_name=
                                     'Значение на конец отчетного периода',)
    diff_reason = models.CharField(max_length=255,
                                   verbose_name=
                                   'Обоснование отклонения фактического значения',)
    
    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)


class TableTwo(models.Model):

    rf_actually = models.FloatField(verbose_name='Референс', null=True)
    rb_actually = models.FloatField(verbose_name='РБ', null=True)
    mb_actually = models.FloatField(verbose_name='МБ', null=True)
    vnb_actually = models.FloatField(verbose_name='ВНБ', null=True)

    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)


class TableThree(models.Model):

    time_execution_actually = models.FloatField(verbose_name='Время по факту',)
    actual_result = models.CharField(max_length=255, verbose_name='Результат',)

    init = models.ForeignKey('InitialData', on_delete=models.CASCADE, null=True)


class InitialData(models.Model):

    indicator_name = models.CharField(max_length=255,
                                      verbose_name='Наименование целевого индикатора')
    unit = models.CharField(max_length=50,
                            verbose_name='Единица измерения')
    plan_value = models.FloatField(verbose_name='План на текущий год')


    event_name = models.CharField(max_length=255,
                                  verbose_name='Наименование мероприятия',)
    rf_set = models.FloatField(verbose_name='Референс',)
    rb_set = models.FloatField(verbose_name='РБ',)
    mb_set = models.FloatField(verbose_name='МБ',)
    vnb_set = models.FloatField(verbose_name='ВНБ',)


    time_execution_plan = models.FloatField(verbose_name='Срок выполнения по плану',)
    expected_result = models.CharField(max_length=255, verbose_name='Ожидаемы результат',)
