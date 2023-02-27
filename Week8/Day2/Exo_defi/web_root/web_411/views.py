from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.http import Http404

# Create your views here.


def index(request,phonenumber):
    try:
        person=Person.objects.get(phonenumber=phonenumber)
        context={
            "phone":person
        }
        return render(request,"posts/pageperson.html",context)
    except Person.DoesNotExist:
        raise Http404("aucune personne ne correspond a ce numero")


def info(request,name):
    try:
        person=Person.objects.get(name=name)
        context={
            "phone":person
        }
        return render(request,"posts/infoperson.html",context)
    except Person.DoesNotExist:
        raise Http404("aucune personne de ce nom")
