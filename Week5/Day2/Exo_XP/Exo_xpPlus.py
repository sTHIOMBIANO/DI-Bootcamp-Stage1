class Family:
    def __init__(self,name_family,member):
      self.name_family=name_family
      self.member=[member]
       
        
    def born(self,**kwargs):
      self.member.append(kwargs)
      print("felicitations a la famille",self.name_family)
      
    def is_18(self,member_name):
        for elem in self.member:
          if elem["name"]==member_name:
            if elem["age"]>18:
              return True
            
            else:
              return False
            
    def family_presentation(self):
        for elem in self.member:
          print(self.name_family,elem["name"])
      

var1= {"name":"Michel","age":35,"gender":"Male","is_child":False}
var2={"name":"Sarah","age":32,"gender":"Female","is_child":True}

var=Family("beogo",var1)
print(var.name_family,var.member)
var.born(name="Sarah",age=7,gender="Male",is_child=False)
var.family_presentation()
print(var.is_18("Sarah"))


class TheIncredibles(Family):
  def __init__(self, name_family, member,power=" ",amazing_name=" "):
    super().__init__(name_family, member)
    self.power=power
    self.amazing_name=amazing_name

  def use_power(self):
    for elem in self.member:
      if elem["age"]>18:
        try:
          print(elem["power"])
        except KeyError:
          print("ils n'ont pas plus de 18ans")
          
          
  def incredible_presentation(self):
    for elem in self.member:
      super().family_presentation()
      print("le pouvoir incroyable de",elem["name"],"est la",elem["power"])
      
var= {"name":"Michel","age":35,"gender":"Male","is_child":False,"power":"fly","amazing_name":"superman"}
var3=TheIncredibles("KI",var)
#print(var3.member)
#var3.use_power()
var3.born(name="Baby Jack",age=25,gender="Male",is_child=False,power="puissance inconnu",amazing_name="mikefly")
print(var3.member)
var3.incredible_presentation()