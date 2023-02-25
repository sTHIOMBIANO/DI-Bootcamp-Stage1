from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path("info/animal/<int:id>/",views.animal,name='animal'),
path("info/family/<int:id>/",views.family,name='family'),
]