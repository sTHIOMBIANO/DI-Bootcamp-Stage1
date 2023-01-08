







M=[
    [' ',' ',' '],[' ',' ',' '],[' ',' ',' ']
]

def display_board():
    print("*"*17)
    for elem in M:
        print("*  ",elem[0],"|",elem[1],"|",elem[2],"  *")
        print("*  ---|---|---  *")
    print("*"*18)
    


def display_play(liste,x):
    #if player1:
    z=int(input("entrer la ligne:"))
    while z>3:
        print("entrer un nombre compris entre 1 et 3 !")
        z=int(input("entrer la ligne:"))
    y=int(input("entrer la colonne:"))
    while y>3:
        print("entrer un nombre compris entre 1 et 3 !")
        y=int(input("entrer la colonne:"))
    if liste[z-1][y-1]==" ":
        liste[z-1][y-1]=x
    else:
        print("cette case est deja rempli" )
    return liste


def verifier(liste):
    if liste[0][0]==liste[0][1]==liste[0][2]=="x":
       
        print("le joueur x gagne !")
            
    elif liste[0][0]==liste[0][1]==liste[0][2]=="o":
        
        print("le joueur o gagne !")
       
    elif liste[1][0]==liste[1][1]==liste[1][2]=="x":
        
       
        print("le joueur x gagne !")
       
    elif liste[1][0]==liste[1][1]==liste[1][2]=="o":
        
        
        print("le joueur o gagne !")
      
    elif liste[2][0]==liste[2][1]==liste[2][2]=="x":
        
        print("le joueur x gagne !")
       
    elif liste[2][0]==liste[2][1]==liste[2][2]=="o":
        
        print("le joueur o gagne !")
       
    elif liste[0][0]==liste[1][0]==liste[2][0]=="x":
       
        print("le joueur x gagne !")
       
    elif liste[0][0]==liste[1][0]==liste[2][0]=="o":
        
        print("le joueur o gagne !")
       
    elif liste[0][1]==liste[1][1]==liste[2][1]=="x":
       
        print("le joueur x gagne !")
       
    elif liste[0][1]==liste[1][1]==liste[2][1]=="o":
        
        print("le joueur o gagne !")
       
    elif liste[0][2]==liste[1][2]==liste[2][2]=="x":
        
        print("le joueur x gagne !")
       
    elif liste[0][2]==liste[1][2]==liste[2][2]=="o":
        
        print("le joueur x gagne !")
       
    elif liste[0][0]==liste[1][1]==liste[2][2]=="x":
       print("le joueur x gagne ")
       
    elif liste[0][0]==liste[1][1]==liste[2][2]=="o":
       print("le joueur o gagne ")
       
    elif liste[2][0]==liste[1][1]==liste[0][2]=="x":
       print("le joueur x gagne ")
       
    elif liste[2][0]==liste[1][1]==liste[0][2]=="o":
       print("le joueur o gagne ")
       
    else:
        print("egalité")
       
def play():
    for i in range(4):
        
        print("player1:")
        display_board()
        display_play(M,"x")
        display_board() 
        
        print("player2:") 
        display_board()
        display_play(M,"o")
        display_board()
    verifier(M)
            
       
        

play()
    
    

