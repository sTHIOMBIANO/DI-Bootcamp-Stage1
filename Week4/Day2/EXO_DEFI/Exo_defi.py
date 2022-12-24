#exercice1

number=int(input("saisir un nombre:"))
longueur=int(input("saisir une longeur:"))
list_multiple=[]
i=1
while i <=longueur:
    nombre=number*i
    list_multiple.append(nombre)
    i+=1
print(list_multiple)


#exercice2
chaine=input("entrer une chaine avec occurence de lettre:")
chaine1=list(chaine)
new=[]
for i in chaine1:
    if i not in new:
        new.append(i)
chaine2="".join(new)
print(chaine2)