# Generated by Django 4.0.10 on 2024-04-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0029_case_suggests_note_suggests_picasso_suggests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='suggests',
            field=models.ManyToManyField(blank=True, help_text='هم می\u200cتوانید خالی بگذارید و هم می\u200cتوانید چند مورد را انتخاب کنید (با نگه\u200cداشتن Ctrl در ویندوز).', null=True, related_name='مناسب برای چه گروهی+', to='cases.suggest'),
        ),
        migrations.AlterField(
            model_name='case',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='هم می\u200cتوانید خالی بگذارید و هم می\u200cتوانید چند مورد را انتخاب کنید (با نگه\u200cداشتن Ctrl در ویندوز).', null=True, related_name='دسته\u200cبندی شکایت اصلی+', to='cases.tag'),
        ),
    ]