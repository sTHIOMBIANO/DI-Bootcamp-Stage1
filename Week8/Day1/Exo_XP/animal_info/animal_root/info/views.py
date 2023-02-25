from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
animals= [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 4,
            "name": "Monkey",
            "legs": 2,
            "weight": 8.6,
            "height":7.27,
            "speed": 36,
            "family": 4
        },
        {
            "id": 5,
            "name": "Snake",
            "legs": 2,
            "weight": 3.67,
            "height":16.2,
            "speed": 55,
            "family": 3
        }

    ]

families= [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id":3,
            "name":"mammifère"
        },
        {
            "id":4,
            "name":"reptile"
        },
        {
            "id":5,
            "name":"insecte"
        },
        {
            "id":6,
            "name":"arachnide"
        },
        {
            "id":7,
            "name":"amphibie"
        }
    ]

def index(request):
    

	context = {
		'animals':animals,
		'families':families
	}
	return render(request,'posts/homepage.html',context)


def animal(request,id):
    liste=[]
    for y in animals:
        if y['family']==id:
            liste.append(y)
    
    context = {
         'animals': liste,
        }
    
            
    return render (request,'posts/page1.html',context)


def family(request,id):
    liste=[]
    for y in animals:
            if y['id']==id:
                liste.append(y)
    
    context = {
         'animals': liste,
        }
    print(context)
    
            
    return render (request,'posts/page2.html',context)