#Exercic1

from math import *
import os
nombre=input("entrer un nombre:")
print("le nombre entrer par un utilisateur",nombre)
n2=float(nombre)
n1=int(n2)
    
if n2:
    print("valur absolue du nombre:",abs(n2))
    print("le nombre entier:",n1)
elif n1:
    print("valur absolue du nombre:",abs(n1))
    print("le nombre entier:",n1)
    
    
    
def __doc__():
    print("la fonction input() permet a un utilisateur d'entrer un nombre.Lorsque celui ci saisit le nombre \n"
          "le nombre est renvoyer sous forme de chaine de caractère.D'ou la syntaxe dans le code. La fonction int()\n"
          "nous permet deconvertir une chaine de caractèreben entier. Ainsi elle peut convertir\n la valeur renvoyée par la fonction input()\n"
          "La fonction abs() comme son nom l'indique est une fonction mathematique permettant \nd'appliquer la valeur absolue a un nombre\n"
          "Pour l'utiliser il faut importer le module math de la bibliothèque standard de python.\n"
          "La syntaxe est dans le code.")


__doc__()
    


os.system("pause")



#Exercic2
class Currency:
    def __init__(self,currency,amount):
        self.currency=currency
        self.amount=amount

    def __str__(self):
        print("'{} {}'".format(self.amount,self.currency))
    
    def __int__(self):
        print("{}".format(self.amount))
        
    def __repr__(self):
         print("{} {}".format(self.amount,self.currency))
         
    def __add__(self,newc):
        if self.currency!=newc.currency:
            print(f"vous ne pouvez pas additionner {self.currency} et {newc.currency} ")
        else:
            print(self.amount+newc.amount,self.currency)
        
        
c1=Currency('dollars',5)
c2=Currency("dollars",15)
c3=Currency("skelel",6)
c1.__str__()
c1.__int__()
c1.__repr__()
c1.__add__(c3)
c1.__add__(c2)