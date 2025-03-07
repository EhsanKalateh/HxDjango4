# Generated by Django 4.0.10 on 2025-03-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0042_case_is_pedi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='case',
            name='setting',
        ),
        migrations.AddField(
            model_name='case',
            name='age_m',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='باقی سن به ماه'),
        ),
        migrations.AlterField(
            model_name='case',
            name='age',
            field=models.PositiveSmallIntegerField(default=40, verbose_name='سن به سال'),
        ),
        migrations.AlterField(
            model_name='case',
            name='dat',
            field=models.TextField(blank=True, help_text='داده\u200cهای آزمایشگاهی و گزارش\u200cهای تصویربرداری، اکوگرافی، نوار قلب و ...', null=True, verbose_name='دیگر داده\u200cها'),
        ),
        migrations.AlterField(
            model_name='case',
            name='source',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='منبع شرح حال'),
        ),
    ]
