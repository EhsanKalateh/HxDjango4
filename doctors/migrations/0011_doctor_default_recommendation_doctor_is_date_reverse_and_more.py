# Generated by Django 4.0.10 on 2025-06-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0010_alter_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='default_recommendation',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_date_reverse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_girl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_who',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='mini_charts_data_count',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='doctor',
            name='redirect_to_print',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctor',
            name='table_rows_count',
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='doctor',
            name='z_score_count',
            field=models.PositiveSmallIntegerField(default=20),
        ),
    ]
