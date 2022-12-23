#exercice1
a="Hello world\n"*4
print(a)

#exercice2
print((99**3)*8)

#exercice3
1=>False
2=>True
3=>False
4=>erreur
5=>True

#exercice4
computer_brand="haitech"
if computer_brand:
    print("j'ai un ordinateur ",computer_brand)


#exercice5
name="THIOMBIANO"
age=24
shoe_size=44
info=print("je me nomme",name,"j\'ai",age,"ans et je porte des shoes d'une pointure de",shoe_size)


#exercice6
a=20
b=17
if a>b:
    print("hello world")

#exercice7
n=int(input("entrer un nombre: "))
if not(n%2):
    print("ce nombre est pair")
else:
    print("ce nombre est impair")

#exercice8
mon_nom="THIOMBIANO"
nom=input("saisissez votre nom: ")
if nom==mon_nom:
    print("Bravo ! nous avons le meme nom")
else:
    print("vous avez un nom different du mien")

#exercice9

taille=int(input("entrer votre taille: "))
if taille>145:
    print("vous etes assez grand pour rouler")
elif taille==145:
    print("vous avez une taille normale pour rouler")
else:
    print("vous devez grandir un peu plus pour rouler")


#exerciceXPGold
print("hello world\n"*4,"\nI love python\n"*4)


#exerciceXPCold1
mois=int(input("saisir un mois entre 1 à 12: "))
if mois==3 or mois ==4 or mois==5:
    print("ce mois est un mois du printemps")
elif mois==6 or mois==7 or mois==8:
    print("ce mois est un mois de l\'été")
elif mois==9 or mois==10 or mois==11:
    print("ce mois est de l\'automne")
elif mois==12 or mois==1 or mois==2:
    print("ce mois est un mois de l\'hiver")
else:
    print("ce type de mois n\'existe pas\nveuillez saisir un nombre compris entre 1 et 12")

