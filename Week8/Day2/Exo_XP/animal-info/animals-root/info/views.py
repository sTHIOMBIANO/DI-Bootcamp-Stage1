from django.shortcuts import render
#from django.http import HttpResponse

from .models import Animal,Family
# Create your views here.

def index(request):
    #if request.method=="GET":
    animal=Animal.objects.all()
    print(animal)
    family=Family.objects.all()

    context={"animals":animal}
    
    return render(request,"posts/animal.html",context)

def animal(request,id):
    animal=Animal.objects.get(id=id)
    context1={
        "animals":animal
        }            

    return render(request,"posts/pageanimal.html",context1)

def family(request,id):
    animal=Animal.objects.filter(familyID=id)
    context={
        "animals":animal
        }            

    return render(request,"posts/pagefamily.html",context)
