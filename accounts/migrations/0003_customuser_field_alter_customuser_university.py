# Generated by Django 4.0.10 on 2024-04-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_degree_alter_customuser_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='field',
            field=models.CharField(blank=True, choices=[('MD/Student', 'MD'), ('Dentist/Student', 'Dent'), ('Nurse/Student', 'Nurse'), ('Other', 'Other'), ('Not Medical Science', 'NMS')], max_length=32),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='university',
            field=models.CharField(blank=True, choices=[('علوم پزشکی مشهد', 'MUMS'), ('علوم پزشکی تهران', 'TUMS'), ('علوم پزشکی خراسان شمالی', 'NKUMS'), ('علوم پزشکی بهشتی', 'SBMU'), ('علوم پزشکی شیراز', 'SUMS'), ('علوم پزشکی ایران', 'IUMS'), ('علوم پزشکی اصفهان', 'MUI'), ('علوم پزشکی گرگان', 'GOUMS'), ('علوم پزشکی گیلان', 'GUMS'), ('علوم پزشکی تبریز', 'TBZMed'), ('علوم پزشکی ساری', 'MazUMS'), ('علوم پزشکی بابل', 'MUBabol'), ('علوم پزشکی جندی\u200cشاپور اهواز', 'AJUMS'), ('علوم پزشکی بقیة\u200cالله', 'BMSU'), ('علوم پزشکی کرمان', 'KMU'), ('علوم پزشکی ارومیه', 'UMSU'), ('علوم پزشکی همدان', 'UMSHa'), ('علوم پزشکی سبزوار', 'MedSab'), ('علوم پزشکی بوشهر', 'BPUMS'), ('علوم پزشکی سمنان', 'SemUMS'), ('علوم پزشکی هرمزگان', 'HUMS'), ('علوم پزشکی کرمانشاه', 'KUMS'), ('علوم پزشکی البرز', 'ABZUMS'), ('علوم پزشکی بیرجند', 'ABZUMS'), ('علوم پزشکی زابل', 'ABZUMS'), ('علوم پزشکی زاهدان', 'ABZUMS'), ('علوم پزشکی یزد', 'SSU'), ('علوم پزشکی شهرکرد', 'SKUMS'), ('علوم پزشکی شاهرود', 'ShMU'), ('علوم پزشکی نیشابور', 'NUMS'), ('علوم پزشکی یاسوج', 'YUMS'), ('علوم پزشکی لرستان', 'LUMS'), ('علوم پزشکی کردستان', 'MUK'), ('علوم پزشکی قم', 'MUQ'), ('علوم پزشکی قزوین', 'QUMS'), ('Other', '----')], help_text='Your current university. Leave empty if not a student.', max_length=30, null=True),
        ),
    ]