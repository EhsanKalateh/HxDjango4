# Generated by Django 4.0.10 on 2024-03-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0011_alter_case_choice_alter_picasso_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='picasso',
            field=models.URLField(blank=True, help_text='می\u200cتوانید لینک کیس مربوط به این تصویر را در اینجا قرار دهید.', null=True, verbose_name='لینک کیس مرتبط'),
        ),
        migrations.AddField(
            model_name='picasso',
            name='case',
            field=models.URLField(blank=True, help_text='می\u200cتوانید لینک کیس مربوط به این تصویر را در اینجا قرار دهید.', null=True, verbose_name='لینک کیس مرتبط'),
        ),
    ]
