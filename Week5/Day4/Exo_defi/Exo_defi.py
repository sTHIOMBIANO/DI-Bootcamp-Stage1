class Text():
    chaine="""Dans notre esprit, c'est surtout en seconde année que l'on cherchera à structurer les connaissances
acquises, en les approfondissant. Les algorithmes seront davantage décortiqués et commentés. Les
projets, cahiers des charges et méthodes d'analyse seront discutés en concertation."""
    def __init__(self,chaine=chaine):
        self.chaine=chaine
        
    #star_list=[]
    def occurrence():
        star_list=[]
        liste="".join(Text.chaine)
        sq_list=liste.split(" ")
        for elem in sq_list:
            if [elem ,sq_list.count(elem)] not in star_list:
                star_list.append([elem,sq_list.count(elem)])
                
        return star_list
    
    def frequence(self,mot):
        maliste=Text.occurrence()
        try:
            i=0 
            while i<len(maliste):
                if maliste[i][0]==mot:
                    print(f"la frequence du mot <<{maliste[i][0]}>> est {maliste[i][1]}")
                    
                i+=1
        except:
            pass
            
           
    def motcourant(self):
        list1=[]
        for elem in Text.occurrence():
            list1.append(elem[1])
        cpt=max(list1)
        for mot in Text.occurrence():
            if mot[1]==cpt:
                print ("le mot le plus courant est",mot[0])
                
            
        
    def Mot_unique(self):
        star_list=Text.occurrence()
        i=0
        listmot=[]
        while i<len(star_list):
            if star_list[i][1]==1:
                listmot.append(star_list[i][0])
                
            i+=1
        print(listmot)
        
    @classmethod
    def renvoyertext(cls):
        with open("Strang.txt",'r') as f:
            content= f.read()
        return cls(content)

chaine1=Text()
#chaine1.frequence('en')
#chaine1.Mot_unique()
#chaine1.motcourant()
print(Text.renvoyertext().chaine)
