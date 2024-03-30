# Generated by Django 4.0.10 on 2024-03-21 13:51

import cases.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0005_case_lang_case_ros_alter_case_phe_alter_case_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picasso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='برای نشان دادن در صفحۀ اصلی.', max_length=50, verbose_name='عنوان')),
                ('description', models.CharField(help_text='خلاصه\u200cای برای نمایش در صفحۀ اصلی', max_length=200, verbose_name='توضیح کوتاه')),
                ('slug', models.SlugField(help_text='برای دسترسی به این تصویر یک آدرس مرتبط ایجاد کنید. برای مثال cushing-striae-01.', verbose_name='لینک')),
                ('text', models.TextField(default='', help_text='متنی کامل دربارۀ تصویر بنویسید. دربارۀ بیماری، دلیل ایجاد این وضعیت و تمام موارد مرتبط.', verbose_name='متن')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=cases.models.user_directory_path)),
                ('premium', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('lang', models.CharField(choices=[('Fa', 'Fa')], default='Fa', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
