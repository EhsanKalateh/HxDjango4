# Generated by Django 4.0.10 on 2024-03-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_alter_case_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='rating',
            field=models.SmallIntegerField(blank=True, choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], null=True),
        ),
    ]