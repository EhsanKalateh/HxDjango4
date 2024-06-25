# Generated by Django 4.0.10 on 2024-06-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0041_alter_case_slug_alter_note_slug_alter_picasso_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='labgraphselection',
            name='zero',
            field=models.BooleanField(default=False, help_text='اگر می\u200cخواهید عدد صفر هم در نمودار درج شود، این تیک را بزنید', verbose_name='رسم از صفر'),
        ),
        migrations.AddField(
            model_name='picasso',
            name='inappropriate',
            field=models.BooleanField(default=False, help_text='اگر این تصویر می\u200cتواند برای بخشی از جامعۀ هدف آزاردهنده باشد، این تیک را بزنید تا به طور واضح در صفحۀ نخست سایت به نمایش در نیاید.', verbose_name='آزاردهنده'),
        ),
    ]
