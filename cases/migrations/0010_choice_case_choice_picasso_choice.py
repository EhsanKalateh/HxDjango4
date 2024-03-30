# Generated by Django 4.0.10 on 2024-03-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0009_case_cover_alter_picasso_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='choice',
            field=models.ManyToManyField(to='cases.choice'),
        ),
        migrations.AddField(
            model_name='picasso',
            name='choice',
            field=models.ManyToManyField(to='cases.choice'),
        ),
    ]