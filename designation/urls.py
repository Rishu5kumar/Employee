from django.urls import path
from . import views

urlpatterns=[
    path('',views.insert_des,name='insert-des'),
    path('show/', views.show_des, name='show-des'),
    path('edit/<int:pk>', views.edit_des, name='edit-des'),
    path('remove/<int:pk>', views.remove_des, name='remove-des'),
]