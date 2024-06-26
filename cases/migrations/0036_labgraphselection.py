# Generated by Django 4.0.10 on 2024-06-10 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0035_comment_liked_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabGraphSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='You can name this selection.', max_length=64)),
                ('data', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.case')),
            ],
        ),
    ]
