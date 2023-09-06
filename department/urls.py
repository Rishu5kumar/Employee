from django.urls import path
from . import views

urlpatterns=[
    path('',views.insert_dept,name='insert-dept'),
    path('show/', views.show_dept, name='show-dept'),
    path('edit/<int:pk>', views.edit_dept, name='edit-dept'),
    path('remove/<int:pk>', views.remove_dept, name='remove-dept'),
]