# Generated by Django 5.1.1 on 2024-09-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_tableone_diff_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabletwo',
            name='mb_actually',
            field=models.FloatField(default=0, verbose_name='МБ'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='mb_set',
            field=models.FloatField(default=0, verbose_name='МБ'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Наименование мероприятия'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='rf_actually',
            field=models.FloatField(default=0, verbose_name='Референс'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='rf_set',
            field=models.FloatField(default=0, verbose_name='Референс'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='total_actually',
            field=models.FloatField(default=0, verbose_name='Всего'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='total_set',
            field=models.FloatField(default=0, verbose_name='Всего'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='vnb_actually',
            field=models.FloatField(default=0, verbose_name='ВНБ'),
        ),
        migrations.AddField(
            model_name='tabletwo',
            name='vnb_set',
            field=models.FloatField(default=0, verbose_name='ВНБ'),
        ),
    ]
