# Generated by Django 4.2.4 on 2023-09-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0011_alter_employee_empgender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpGender',
            field=models.IntegerField(max_length=150),
        ),
    ]
