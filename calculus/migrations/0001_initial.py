# Generated by Django 4.0.10 on 2025-03-28 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalCate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Calculi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('link', models.SlugField(max_length=64, unique=True)),
                ('html', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculus.calcate')),
            ],
        ),
    ]
