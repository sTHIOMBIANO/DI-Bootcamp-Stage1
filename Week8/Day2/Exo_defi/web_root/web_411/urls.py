from django.urls import path
from . import views

urlpatterns=[
    path("persons/<int:phonenumber>",views.index,name='index'),
    path("persons/<str:name>",views.info,name='info')
]