matrix=[
    ["7","T","h","i","s","$","#","^"],
    ["i","s","%"," ","M","a","t","r"],
    ["3","i","x","#"," "," ","%","!"]
    ]
def Matrix(l):
    liste=[]
    for elem in l:
        for letter in elem:
            if letter.isalpha():
                liste.append(letter)
            else:
                liste.append(' ')
    i=0
    while i <len(liste):
        if liste[i]==" ":
            del(liste[i])
        i+=1
    chaine="".join(liste)
    #print(liste)
    print(chaine)
    
    
var=Matrix(matrix)

