# Generated by Django 4.0.10 on 2024-03-31 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='Visibility'),
        ),
    ]
