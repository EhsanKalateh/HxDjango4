# Generated by Django 4.0.10 on 2024-04-01 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0025_remove_case_picasso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=True)),
                ('done', models.BooleanField(default=True)),
                ('lang', models.CharField(choices=[('Fa', 'Fa')], default='Fa', max_length=2)),
                ('rating', models.SmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('title', models.CharField(help_text='برای نشان دادن در صفحۀ اصلی.', max_length=50, verbose_name='عنوان')),
                ('description', models.CharField(help_text='خلاصه\u200cای برای نمایش در صفحۀ اصلی', max_length=200, verbose_name='توضیح کوتاه')),
                ('text', models.TextField(default='', help_text='اینجا در اختیار شماست تا تمام متن خود را بنویسید.', verbose_name='متن')),
                ('slug', models.SlugField(help_text='برای دسترسی به این یادداشت یک آدرس مرتبط ایجاد کنید. برای مثال ems-01.', verbose_name='لینک')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('delete', models.BooleanField(default=False, verbose_name='I want to DELETE this Ex.')),
                ('editors_review', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('choice', models.ManyToManyField(blank=True, null=True, to='cases.choice')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='cases.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default='', verbose_name='متن')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suggest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.DeleteModel(
            name='Rien',
        ),
        migrations.AddField(
            model_name='picasso',
            name='editors_review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
