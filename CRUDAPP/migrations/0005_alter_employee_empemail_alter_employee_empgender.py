# Generated by Django 4.2.4 on 2023-09-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0004_alter_employee_empemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpEmail',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpGender',
            field=models.CharField(max_length=200),
        ),
    ]
