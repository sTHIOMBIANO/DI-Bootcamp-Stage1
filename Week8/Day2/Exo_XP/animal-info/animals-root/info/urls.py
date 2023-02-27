from django.urls import path
from . import views

urlpatterns=[
    path('animal/',views.index,name='index'),
    path('animal/<int:id>',views.animal,name='animal'),
    path('family/<int:id>',views.family,name='family'),
]