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
