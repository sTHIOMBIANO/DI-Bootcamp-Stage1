from django.urls import path
from . import views

urlpatterns=[
    path('people/',views.index,name="index"),
    path('people/<int:id>',views.info,name='info')
]