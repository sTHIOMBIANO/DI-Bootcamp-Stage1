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




mot="hello world"
for i in range(len(mot)+1):
        print(mot[0:i])

chaine=mot.replace('ello ','lrole')
print(chaine)




