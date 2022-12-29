import os

#exercice1
mot=input("entrer un mot:")

#mot_list=list(mot)
dict_mot={}


for elem in mot:
    list_index=[]
    for i in range(len(mot)):
        if elem==mot[i]:
            list_index.append(i)
            
    dict_mot[elem]=list_index
      
       

#print(list_index)
#print(mot_list)
print(dict_mot)


os.system("pause")

#exercice2

wallet=int(input("entrer juste la somme de votre wallet en entier:"))


dictio_article={"Water":1,"Bread":3,"TV":1000,"Fertilizer":20,"Apple":4,"Honey":3,"Fan":14,"Bananas":4,"Pan":100,"Spoon":2,"phone":999,"Speakers":300,"Laptop":5000,"PC":1200}
list_article=[]
if wallet >1:
    for cle,valeur in dictio_article.items():
        for i in range(len(dictio_article)): 
            if valeur < wallet:
                list_article.append(cle)
            break
    liste=sorted(list_article)
    print(liste)
else:
    print("Rien")
    



    