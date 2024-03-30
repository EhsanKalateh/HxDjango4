# Generated by Django 4.0.10 on 2024-03-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='slug',
            field=models.SlugField(help_text='لینک مورد علاقه برای کیس خود را وارد کنید. تلاش کنید لینکتان گویا و دقیق باشد، پس از این توانایی تغییر آن را نخواهید داشت. استفاده از فاصله (Space) مجاز نیست.', max_length=40, unique=True, verbose_name='Link'),
        ),
    ]