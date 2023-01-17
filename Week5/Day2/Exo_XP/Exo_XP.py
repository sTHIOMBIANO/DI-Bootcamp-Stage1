import os

class Pets():
    def __init__(self,animals):
        self.animals=animals
class Cat:
    is_lazy=True
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    def walk(self):
        return f'{self.name} is just walking around'
    
    
class Bengal(Cat):
    def sing(self,sounds):
        return f'{sounds}'
    
class Chartreux(Cat):
    def sing(self,sounds):
        return f'{sounds}'
    
    
class Siamese(Cat):
    pass

all_cats=[]
animal1=Bengal("caline",12)
all_cats.append(animal1.name)
animal2=Chartreux("millie",7)
all_cats.append(animal2.name)
animal3=Siamese("canelle",3)
all_cats.append(animal3.name)
#print(animal1.name)


sara_pets=Pets("chien")
sara_pets=all_cats
#print(sara_pets.animals)
#all_cats.append([sara_pets.animals])
#print(all_cats)
print(sara_pets)
for elem in sara_pets:
    sara_pet=Cat(elem,4)
    sara=Bengal(elem,3)
    print(sara_pet.walk())
    print(sara.sing("aboie"))
    #sara_pets.walk()
    #print(sara_pet)
    
    
os.system("pause")
    
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        
    def bark(self):
        return f'{self.name} aboie'
    
    def run_speed(self):
        self.vitesse= self.weight/(self.age*10)
        return self.vitesse
    
    def fight(self,other_dog):
        if self.vitesse*self.weight > other_dog.vitesse*other_dog.weight:
            print(f"{self.name} a gagné le combat")
        else:
            print(f"{other_dog.name} a gagné le combat")
        
chien1=Dog("Milou",3,18)
chien2=Dog("Rex",5,100)
chien3=Dog("Djamond",8,20)

print(chien1.bark())

(chien1.run_speed())
chien2.run_speed()
chien3.run_speed()
chien1.fight(chien2)

    
    
    

        