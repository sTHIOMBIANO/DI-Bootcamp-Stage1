
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
    
    while liste[z-1][y-1]!=" ":
        print("Reprenez la case est occupée")
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
            break
    else:
        liste[z-1][y-1]=x

       
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
        exit()
       
    elif liste[0][0]==liste[1][0]==liste[2][0]=="x":
       
        print("le joueur x gagne !")
        exit()
    elif liste[0][0]==liste[1][0]==liste[2][0]=="o":
        
        print("le joueur o gagne !")
        exit()
    elif liste[0][1]==liste[1][1]==liste[2][1]=="x":
       
        print("le joueur x gagne !")
        exit()
    elif liste[0][1]==liste[1][1]==liste[2][1]=="o":
        
        print("le joueur o gagne !")
        exit()
    elif liste[0][2]==liste[1][2]==liste[2][2]=="x":
        
        print("le joueur x gagne !")
        exit()
    elif liste[0][2]==liste[1][2]==liste[2][2]=="o":
        
        print("le joueur x gagne !")
       
    elif liste[0][0]==liste[1][1]==liste[2][2]=="x":
       print("le joueur x gagne ")
       exit()
    elif liste[0][0]==liste[1][1]==liste[2][2]=="o":
       print("le joueur o gagne ")
       exit()
    elif liste[2][0]==liste[1][1]==liste[0][2]=="x":
       print("le joueur x gagne ")
       exit()
    elif liste[2][0]==liste[1][1]==liste[0][2]=="o":
       print("le joueur o gagne ")
       exit()
   
       
def play():
    print("                  ")
    print("Bienvenue sur Tic Tack Toe")
    print( "                   ")
    i=0
    cpt=1
    while i<=5:
        if not verifier(M):
            
            
            display_board()
            print("           ")
            print("player1:")
            display_play(M,"x")
            display_board()
            cpt+=1
            if cpt==10:
                if verifier(M):
                    exit()
                else:
                    print("égalité")
                    exit()
             
            display_board()
            print("               ")
            print("player2:")
            display_play(M,"o")
            display_board()
            #verifier(M)
            cpt+=1
            if cpt==11:
                print("égalité")
                exit()  
        elif verifier(M):
            exit()
        
          
            
        i+=1
        
       
        

play()
    
    

