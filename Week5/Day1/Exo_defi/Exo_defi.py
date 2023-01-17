class Farm:
    def __init__(self,name):
        self.name=name
        self.liste={}
    
    def add_animal(self,name,compteur=1):
        if name in self.liste:
            self.liste[name]=compteur+compteur
        else:
            self.liste[name]=compteur
        
    def get_info(self):
        for cle,valeur in self.liste.items():
            print(f"{cle}:\t{valeur}")
            
    def get_animals_types(self):
        self.sq_list=[]
        for cle in self.liste.keys():
           self.sq_list.append(cle)
           nom_animal=sorted(self.sq_list)
        return (nom_animal)
        
    def get_short_info(self):
        animal=",des ".join(self.get_animals_types())
        print(f"La ferme McDonald possede des {animal}")
            
            
        
            
macdonald=Farm("McDonald")
macdonald.add_animal("cow",5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat",12)
macdonald.get_info()
print(macdonald.get_animals_types())
macdonald.get_short_info()