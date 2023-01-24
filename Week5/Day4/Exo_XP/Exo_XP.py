#exercice

def get_words_from_sowpods():
    with open("sowpods.txt","r") as f:
        content=f.readlines()
        sq_list="".join(content)
        start_list=sq_list.split("\n")
    return start_list

#get_words_from_sowpods()
print("le type de données correct pour stocker les mots est le type liste")

#exercice
import random
def get_random_sentence(length=5):
    liste=get_words_from_sowpods()
    i=0
    phrase=''
    while i<length:
        mot=random.choice(liste)
        phrase+=' '+mot
        i+=1
    print(phrase)
    return phrase

#get_random_sentence(5)
phrase=(get_random_sentence(5))
phrase=phrase.lower()+"."
#print(phrase)

def main():
    print("la fonction get_words_from_sowpods lit le contenu du\n fichier et le renvoie sous forme de liste")
    print("la fonction get_random_sentence() prend un nombre en\n parametre et renvoie un nombre de mots egale a la taille du mot en parametre")
    print("la valeur par de defaut de ctte fonction est 5")
    
    tmp=abs(int(input("combien de temps voulez vous que la phrase dure:")))
    if tmp==1 or tmp==2 or tmp==20:
        code=phrase
        print(code)
    else:
        print("Error ,vous avez saisi des données incorrectes")
        exit()

#main()
#exercice2


import json

samplejson={
    "compagny":{
        "employee":{
            "name":"emma",
            "paysable":{
                "salary":7000,
                "bonnus":800
                }
            }
        }
    }

print(samplejson["compagny"]["employee"]["paysable"]["salary"])
samplejson["compagny"]["employee"]["birth_date"]="15-3-2000"
print(samplejson)
json_file="data.json"
with open(json_file,'w') as file:
    json.dump(samplejson,file,indent=2,sort_keys=True)
    
with open(json_file,'r') as f:
    dictio=json.load(f)
print(dictio)