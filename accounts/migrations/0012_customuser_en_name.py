# Generated by Django 4.0.10 on 2024-09-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_customuser_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='en_name',
            field=models.BooleanField(default=True),
        ),
    ]