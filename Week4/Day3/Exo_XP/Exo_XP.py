import os


#exercice1


dictio=dict(zip(['Ten','Twenty','Thirty'],[10,20,30]))
print(dictio)


os.system("pause")

#exercice2

family={"rick":43,"beth":13,"morty":5,"summer":8,}
ng=nb=nb1=0
for elem in family.values():
    if elem<3:
        for (k,val) in family.items():
            if val==elem:
                nom=k
        print(nom ,"va payer 0$")
        ng+=1
    elif 3<=elem<12:
        for (k,val) in family.items():
            if val==elem:
                nom=k
        print(nom ,"va payer 10$")
        nb+=1
    elif elem>=12:
        for (k,val) in family.items():
            if val==elem:
                nom=k
        print(nom,"va payer 15$")
        nb1+=1
cout_total=(nb*10)+(nb1*15)
print("le cout total de la famille est:",cout_total,"$")

os.system("pause")

family={}
nb=int(input("entrer le nombre de personnes de la famille:"))

for i in range(nb):
    nom=input("entrer le nom:")
    age=int(input("entrer l'age:"))
    if nom!="" and age!="":
        family[nom]=age
    
   
print(family)
os.system("pause")

#exercice3

band={'nom':'Zara','creation_date':1975,'creator_name':['Amancio','Ortega','Gaona'],'type_of-clothes':['men','women','children','home'],'international_competitors':['Gap','H&M','Benetton'],'number_stores':7000,'France':'blue','Spain':'red','US':['pink','green']}

band['number_stores']=2

print("les clients de Zaras sont",band['type_of-clothes'])

band['country_creation']='Spain'

if ('international_competitors' in band):
    print('la cle existe dans le dictionnaire !')
    band['international_competitors'].append('Desigual')
else:
    print("la cle n'existe pas dans ce dictionnaire !")
    
del(band['creation_date'])

print(band['international_competitors'][-1])

print(band['US'])

print(len(band))

print(band.keys())
#print(band)

more_on_zara={'creation_date':1975,'number_stores':10000}
band.update(more_on_zara)
print("la valeur du dernier:",band['number_stores'])

"la valeur de la clé number_stores a pris la valeur conenu dans le diction more_on_zara"

os.system("pause")


#exercice4


users=["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A={}
disney_users_B={}
disney_users_C={}

for n in range(len(users)):
    for elem in users:
        disney_users_A[elem]=n
        disney_users_B[n]=elem
       
       
for k in sorted(disney_users_A.keys()):
    disney_users_C[k]=disney_users_A[k]
print(disney_users_A)
print(disney_users_B)
print(disney_users_C)





disney_user={}
disney_user_MP={}
for n in range(len(users)):
    for elem in users:
        for j in elem:
            if j=='i':
                disney_user[elem]=n
        
        if elem[0]=='M' or elem[0]=='P':
            disney_user_MP[elem]=n
        
print(disney_user)
print(disney_user_MP)  