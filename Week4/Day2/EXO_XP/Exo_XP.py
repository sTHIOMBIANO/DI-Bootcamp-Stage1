#exercice1

my_fav_numbers=set([63237266,58330367])

my_fav_numbers.add("77278533")
my_fav_numbers.add("60128168")

my_fav_numbers.pop()


freind_fav_number={"55555556","67676789"}

our_fav_number=my_fav_numbers | freind_fav_number

print(my_fav_numbers)
print(our_fav_number)

#exercice2

"""non il n'est pas possible d'ajouter un entier a un tuple car les tuples sont immuable cela signifie qu'ils ne sont pas modifiable"""


#exercice3

basket=["banane","Myrtilles","Apples","Orages","Blueberries"]

#basket.remove("banane")
del(basket[0])

del(basket[0])

basket.append("Kiwi")

basket.insert(0,"pommes")

nb=basket.count("pommes")

basket.clear()

print(nb)
print(basket)



#exercice4

"""un float est un nombre réel plus précisement un nombre a virrgule
la difference est qu'un nombre entier est sans virrgule et est de type int"""

"""oui en utulisant le module numpy appliqué a la fonction 
arange qui prend en parametre trois elements"""

flottant=[1.5,2,2.5,3,3.5,4,4.5,5]
print(flottant)


#exercice5

for i in range(1,21):
    print(i)

for j in range(1,20):
    print(j)



#exercice6

continuer=True
mon_nom="THIOMBIANO"
while continuer:
    nom=input("entrer votre nom: ")
    if nom==mon_nom:
        continuer=False


#exercice7

chaine=input("saisir la liste de tes fruits préférés en mettant des espaces entre les fruits saisis: \n")
list1=chaine.split(" ")
fruit=input("saisir votre fruit préféré: ")
for i in list1:
    if i==fruit:
        print("vous avez choisi l'un de vos fruits préféré.Prendre plaisir !")
        break
    else:
        print("vous avez choisi un nouveau fruit.J'espere que vous appréciéz !")
        break

print(list1)


#exercice8

continuer=True
Total=0
start_list=[]
while continuer:
    pizza=input("entrer une garniture pizza: " )
    print("vous ajouterez cette garniture a votre pizza")
    Total+=12.5
    start_list.append(pizza)
    if pizza=="quitter":
        continuer=False
print("liste de garniture entrer:",start_list,"\nTalal prix:",Total)

#exercice9

age=int(input("quel est votre age: "))
if age<3:
    billet=0
elif 3<=age<=12:
    billet=10
elif age>12:
    billet=15



continuer=True
ng=nb=nb1=0
i=0
nombre=int(input("quel est le nombre de personnes de la famille:"))
while i<=nombre:
    age=int(input("quel est votre age: "))
    quitter=input("voulez vous un billet ? validez par o/n:")
    if quitter=="o" or quitter=="O":
        if age<3:
            ng+=1
        elif 3<=age<=12:
            nb+=1
        elif age>12:
            nb1+=1
    else:
        ng=ng
        nb=nb
        nb1=nb1
    i+=1
cout_total=(ng*0)+(nb*10)+(nb1*15)
print("le cout total est:",cout_total,"$")




sq_list=["Ali","Bertrand","Simon","Armelle","Sidiki","Issa","Mohamed"]
for i in range(len(sq_list)):
    age=int(input("quel est votre age:"))
    if age<16 or age>21:
        del(sq_list[i])
print("la liste du groupe qui peut acceder a la salle:",sq_list)




#exercice10

sandwich_order=["Tuna sandwich","Avoca sandwich","Egg sandwich","Sabih sandwich","Pastrami sandwich"]
finised_sandwich=[]
i=0
while i < (len(sandwich_order)):
    mot=sandwich_order[i]
    del(sandwich_order[i])
    finised_sandwich.append(mot)
i+=1
if sandwich_order==[]:
    print("I made your tuna sandwich")






#exercice11

sandwich_order=["Tuna sandwich","Pastrami sandwich","Avoca sandwich","Pastrami sandwich","Egg sandwich","Sabih sandwich","Pastrami sandwich"]
finised_sandwich=[]
print("l'epicerie est à cours de pasrtami")
i=0
while i <len(sandwich_order):
    if sandwich_order[i]=="Pastrami sandwich":
        del(sandwich_order[i])
    i+=1
finised_sandwich=sandwich_order
print(sandwich_order)
print(finised_sandwich)