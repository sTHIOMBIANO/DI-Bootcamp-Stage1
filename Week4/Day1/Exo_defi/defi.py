import random
import os


#1.2.
chaine=input("saisir une chaine de caractere: ")
first=chaine[0]
last=chaine[-1]
if len(chaine)<10:
    print("chaine pas assez long !")
elif len(chaine)>10:
    print("chaine trop longue !")
elif len(chaine)==10:
    print("la chaine comporte 10 caractères !")
print("premier caractère:",first,"\ndernier caractèere:",last)

os.system("pause")


#3.for loop
mot=chaine
for i in range(len(mot)+1):
        print(mot[0:i])


os.system("pause")


#4.Bonnus

chaine=chaine.replace(" ","")
chaine1=list(chaine)
random.shuffle(chaine1)
chaine2="".join(chaine1)
print(chaine2)




