# Generated by Django 4.2.4 on 2023-09-17 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designation', '0003_remove_designation_des_id_alter_designation_des_name'),
        ('CRUDAPP', '0022_remove_employee_empdepartment_employee_empdepartment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='EmpDesignation',
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='designation.designation'),
            preserve_default=False,
        ),
    ]