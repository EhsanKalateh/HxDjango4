# Generated by Django 4.0.10 on 2024-03-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0021_rien_rename_caseimage_imagecase_remove_case_choice_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rien',
        ),
        migrations.RemoveField(
            model_name='case',
            name='BP_D',
        ),
        migrations.RemoveField(
            model_name='case',
            name='BP_S',
        ),
        migrations.RemoveField(
            model_name='case',
            name='PR',
        ),
        migrations.RemoveField(
            model_name='case',
            name='RR',
        ),
        migrations.RemoveField(
            model_name='case',
            name='SPO2_N',
        ),
        migrations.RemoveField(
            model_name='case',
            name='SPO2_O',
        ),
        migrations.RemoveField(
            model_name='case',
            name='Temp',
        ),
        migrations.AddField(
            model_name='case',
            name='choice',
            field=models.ManyToManyField(blank=True, null=True, related_name='Choice', to='cases.choice'),
        ),
        migrations.AddField(
            model_name='case',
            name='done',
            field=models.BooleanField(blank=True, null=True,default=True),
        ),
        migrations.AddField(
            model_name='case',
            name='premium',
            field=models.BooleanField(blank=True, null=True,default=False),
        ),
        migrations.AddField(
            model_name='case',
            name='visible',
            field=models.BooleanField(blank=True, null=True,default=True),
        ),
        migrations.AddField(
            model_name='picasso',
            name='done',
            field=models.BooleanField(blank=True, null=True,default=True),
        ),
        migrations.AddField(
            model_name='picasso',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='cases.tag'),
        ),
        migrations.AddField(
            model_name='picasso',
            name='visible',
            field=models.BooleanField(blank=True, null=True,default=True),
        ),
    ]
