# Generated by Django 4.2.4 on 2023-09-15 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDAPP', '0012_alter_employee_empgender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='EmpGender',
        ),
    ]
