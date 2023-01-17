from Exo_XP import Dog
import random


class PetDog(Dog):
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.trained=trained

    def train(self):
        print(self.bark())
        self.trained=True
        
    def play(self,*args):
        print(f"{args} tous jouent ensemble")
        
    def do_a_trick(self,dog_name):
        var1= random.choice("cedf")
        if var1=="c":
            print(f" {dog_name} fait un tonneau")
        elif var1=="e":
            print(f"{dog_name} se dresse sur ses pattes")
        elif var1=="d":
            print(f"{dog_name} se serre la main")
        else:
            print(f"{dog_name} fait la mort")
       
        
        
var=PetDog("milou",4,7)
var.do_a_trick(var.name)
var.play("wafel","rex","milou")
var.train()