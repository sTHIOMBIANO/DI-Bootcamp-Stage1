class Cat:
    def __init__(self,cat_name,cat_age):
        self.name=cat_name
        self.age=cat_age
        
chat1=Cat("Caline",15)
chat2=Cat("Millie",10)
chat3=Cat("Cannelle",12)
print(chat1.name,chat1.age)

def ancien():
    if chat1.age>chat2.age:
        if chat2.age>chat3.age:
            return chat1
        else:
            return chat1
    elif chat2>chat1:
        if chat1>chat3:
            return chat2
        else:
            return chat2
    else:
        return chat3

chat=ancien()
print("le chat le plus agé est",chat.name,"et à",chat.age,"ans")
    

#ancien()


class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height
        
    def bark(self):
        print(f"{self.name} va woof !")
        
    def jump(self):
        x=self.height*2
        print(f"{self.name} saute {x} en cm de haut")
        
        
davids_dog=Dog("Rex",50)
print("nom du chien:",davids_dog.name,"\ntaille du chien:",davids_dog.height,"cm")
davids_dog.bark()
davids_dog.jump()
   
sarahs_dog=Dog("Teacup",20)
print("nom du chien:",sarahs_dog.name,"\ntaille du chien:",sarahs_dog.height,"cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height>sarahs_dog.height:
    print("le chien le pls grand est:",davids_dog.name)
else:
    print("le chien le plus grand est:",sarahs_dog.name)
    
    
    
    

class Song:
    
    def __init__(self,lyrics):
        self.lyrics=lyrics
        #self.lyrics.append(self)
    def sing_me_a_song(self):
        for elem in self.lyrics:
            print(elem)
            
stairway=Song(["there is a lady who's sure","all glitters is gold","and she's buyinga stairway to heaven"])

stairway.sing_me_a_song()

"""
class Zoo:
    
    def __init__(self,zoo_name):
        self.animals=[]
        self.name=zoo_name
    
    def add_animal(self,new_animal):
        
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animal(self):
        for elem in self.animals:
            print(elem.name)
            
    def sell_animal(self,animal_sold):
        if animal_sold not in self.animals:
            print("cet animal n'est pas dans la liste")
        else:
            self.animals.remove(animal_sold)
            
an=Zoo("Faso parc")
an.add_animal("lion")
an=Zoo("chat")
an.add_animal(an)
an.get_animal()
an.get_animal()
an.sell_animal"""
