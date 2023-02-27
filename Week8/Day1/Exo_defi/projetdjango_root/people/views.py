from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
peuple = [
    {
        'id': 1,
        'name': 'Bob Smith',
        'age': 35,
        'country': 'USA'
    },
    {
        'id': 2,
        'name': 'Martha Smith',
        'age': 60,
        'country': 'USA'
    },
    {
        'id': 3,
        'name': 'Fabio Alberto',
        'age': 18,
        'country': 'Italy'
    },
    {
        'id': 4,
        'name': 'Dietrich Stein',
        'age': 85,
        'country': 'Germany'
    }]




def index(request):

    
    
    liste=sorted(peuple,key=lambda people:people['age'])
    context={
    'people':liste,
    }
    return render(request,"posts/people.html",context)


def info(request,id):
    
    for elem in peuple:
        if elem['id']==id:
            liste=elem
    context={
        'info':liste,
    }
    return render(request,"posts/info.html",context)