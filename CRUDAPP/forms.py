from django import forms

from .models import Employee
from django.core.exceptions import ValidationError
from department.models import Department
from designation.models import designation

# DESIGNATION_CHOICES = [
#     (-1, 'Select Designation'),
#     (1, 'Project Manager'),
#     (2, 'Web Developer'),
#     (3, 'Scrum Master'),
#     (4, 'Programmer'),
#     (5, 'Android Developer')
# ]
# Department=[
#     (-1,'select department'),
#     (1,'CSE'),
#     (2,"CST"),
#     (3,"CEN"),
#     (4,"ECE"),
#     (5,"EEE"),
#     (6,"EIE"),
# ]

GENDER_CHOICES = [(1, 'Male'), (2, 'Female'), (3, 'Others')]


class EmployeeForm(forms.Form):
    EmpId = forms.CharField(required=True, max_length=3, help_text="only numbers allowed")
    EmpName = forms.CharField(required=True, max_length=200)
    EmpGender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    EmpEmail = forms.EmailField(required=True,max_length=255)
    EmpDepartment=forms.MultipleChoiceField(required=True)
    designation = forms.ChoiceField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        depts = Department.objects.values_list('id', 'EmpDept')
        self.fields['EmpDepartment'].choices = depts

        desigs=designation.objects.values_list('id','des_name')
        self.fields['designation'].choices=desigs


class EditForm(forms.Form):
    EmpEmail = forms.EmailField(required=True)
    EmpDepartment = forms.MultipleChoiceField(required=True)
    designation = forms.ChoiceField(required=True)
    #EmpDesignation = forms.ChoiceField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        depts = list(Department.objects.values_list('id', 'EmpDept'))
        self.fields['EmpDepartment'].choices = depts
        desigs=list(designation.objects.values_list('id','des_name'))
        self.fields['designation'].choices=desigs


# def clean_EmpDesignation(self):
#         value = self.cleaned_data["EmpDesignation"]
#         if value == '-1':
#             raise ValidationError('Invalid Choice')

# def clean_Empdepartment(self):
#     value=self.cleaned_data['EmpDepartment']
#     if value=='-1':
#         raise ValidationError('Invalid Department')
