# Generated by Django 4.0.10 on 2024-03-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_md',
            field=models.BooleanField(default=True, verbose_name='MarkDown Active'),
        ),
    ]
