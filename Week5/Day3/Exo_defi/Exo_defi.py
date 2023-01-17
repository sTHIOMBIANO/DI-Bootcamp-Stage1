from math import *
from operator import attrgetter

class Circle:
    
    liste={}
    def __init__(self,nom,rayon):
        self.nom=nom
        self.rayon=rayon
        
        
        
    def additionner(self,new_circle):
        return self.nom+new_circle.nom ,self.rayon+new_circle.rayon
    
    def surface(self):
        print("la surface est ",pi*self.rayon**2)
    
    def comparer(self,new_circle):
        if self.rayon>new_circle.rayon:
            print(f"the circle {self.nom} is gritter than the circle {new_circle.nom}")
        elif self.rayon==new_circle.rayon:
            print("the two circle are equal")
        else:
            print(f"the circle {new_circle.nom} is bigger than the circle {self.nom}")
    
    def ajouter(self):
       
        self.liste[self.nom]=self.rayon
        sq_list=[]
        for cle in self.liste.keys():
            sq_list.append(cle)
        sq_list.sort()
        print(self.liste)
        print("la liste est trié par nom de cercle:",sq_list)

c1=Circle("Horir",5)
c2=Circle("Bonbon",8)
c3=Circle("Kaka",6)
c1.surface()
print(c2.additionner(c1))
c3.ajouter()
c2.ajouter()
c1.ajouter()


c1.comparer(c2)
