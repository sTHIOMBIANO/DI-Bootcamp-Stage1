from random import *
import os


#Exercice1
def display_message():
    print("Dans ce cours j'apprend les bases bases et les fondamentaux du language python")


var=display_message()

os.system("pause")

#Exercice2

def favorite_book(title):
    print("l'un de mes livres préférés est",title)

favorite_book("Camara Laye,l'enfant noir")


os.system("pause")


#Exercice3
def describe_city(nom_ville="Fada N'gourma",pays="Burkina Faso"):
    print(nom_ville,"se trouve dans ",pays)

var=describe_city()


os.system("pause")
#Exercice4

def nombre(nb):
    if 1<=nb<=100:
        x=randint(1,100)
        if nb==x:
            print("reussite")
        else:
            print("echec")
    elif nb<1 or nb>100:
        print("le nombre doit etre compris entre 1 et 100")  

var=nombre(105)


os.system("pause")


#Exercice5
"""
def make_shirt(taille,text):
    text="made in Burkina Faso"
    print("la taille du shirt est ",taille,"et le text est",text)
    
var=make_shirt("S",' ')"""


def make_shirt(taille="XL",text="j'aime python"):
    #text="made in Burkina Faso"
    print("la taille du shirt est ",taille,"et le text est",text)
    
    
grande_chemise=make_shirt("XXL")
chemise_moyenne=make_shirt("XL")
taille_chemise=make_shirt("L")

os.system("pause")


#Exercice6

def show_magiciens(magicien):
    for nom in magicien:
        print(nom)

magiciens_name=['Harry Houdini','David Blaine','Criss Angel']
show_magiciens(magiciens_name)



def make_Great(magicien):
    liste=[]
    text="the great"
    for name in magicien:
        nom=name+" "+text
        liste.append(nom)
    print (liste)

magiciens_name=['Harry Houdini','David Blaine','Criss Angel']
make_Great(magiciens_name)

os.system("pause")

#Exercice7


from random import *

def get_random_temp():
    return randint(-10,40)

x=get_random_temp()
print(x)


def main():
    x=get_random_temp()
    print("la temperature actuelle est de",x,"dégrés celsius")
    if x<=0:
        print("c'est glacial")
    elif 0<x<=16:
        print("c'est assez froid ,n'oubliez pas votre manteau")
    elif 16<x<=23:
        print("il ne fait plus froid,vous pouvez enlever vos manteau")
    elif 23<x<=32:
        print("il fait assez chaud")
    elif 32<x<=40:
        print("la chaleur devient insuportable,activez le climatiseur")
        
        
var=main()

os.system("pause")


def get_random_temp(saison):
    
    if saison=='hiver':
        x= randint(-10,16)
        print("la temperature est",x,"°c")
    elif saison=="printemps":
        x= randint(17,25)
        print("la temperature est",x,"°c")
    elif saison=="été":
        x= randint(26,34)
        print("la temperature est",x,"°c")
    elif saison=="automne":
        x= randint(35,40)
        print("la temperature est",x,"°c")

saison=input("saisir une saison:")
get_random_temp(saison)
    
os.system("pause")
    


#print(y)


def main():
   
   
    if mois==1 or mois==2 or mois==12:
        y=uniform(-10,16)
        print("la temperature actuelle est",y,"°c")
        print("c'est l'hiver")
    elif 3<=mois<=5:
        y=uniform(30,40)
        print("c'est l'automne")
        print("la temperature actuelle est",y,"°c")
    elif 6<=mois<=8:
        y=uniform(20,30)
        print("c'est le primptemps")
        print("la temperature actuelle est",y,"°c")
    elif 9<=mois<=11:
        y=uniform(16,20)
        print("c'est l'été")
        print("la temperature actuelle est",y,"°c")
    
mois=int(input("entrer le numero du mois entre 1 et 12:"))
main()

os.system("pause")
