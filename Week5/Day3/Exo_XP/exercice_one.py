from func import ajouter
import random,string,datetime,time
#exercice2


def nombre():
    nb=int(input("entrer un nombre:"))
    while 1<=nb>=100:
        print("la fonction accepte un nombre compris un nombre entr 1 et 100\n veuillez reprendre la saisie !")
        nb=int(input("entrer le nombre:"))
    x=random.randint(1,100)
    if nb==x:
        print("Reussite !")
        

#exercice3




def getchaine(long=5):
    str1=string.ascii_lowercase
    str2=string.ascii_uppercase
    str=str1+str2
    x=''
    for i in range(long):
        
        x+= ''.join(random.choice(str))
    return x
    

print(getchaine())


#exercice4

def todaydate():
    date=datetime.datetime.now()

    print(date)
    
todaydate()

#exercice5

def display_date():
    before=datetime.datetime.now()
    
    an=before.year+1
    after=datetime.datetime(an,before.month,abs(before.day-(before.day-1)))
    print(f"le 1er janvier est dans {after-before}")
    
    

display_date()
#exercice6
import math

def get_naissance():
    date_naissance=input("entrer votre date de naissance sous la forme aa-mm-jj:").split("-")
    dat=datetime.date(int(date_naissance[0]),int(date_naissance[1]),int(date_naissance[2]))
    dt1=datetime.date.today()
    #dt2=datetime.strptime("22 Oct 2021","%d/%m/%y")
    jour_vecu=math.trunc((dt1-dat).days*(24*60))
    
    print(f" vous avez vecu {jour_vecu} minutes")
   

get_naissance()


#exercice7

def today_date():
    x=datetime.date.today()
    print("la date d'aujourd'hui c'est",x.strftime("%A %d %B %y"))
    y=datetime.date(x.year,x.month+2,x.day)
    z=y-x
    print(y)
    print("les prochains congés sont dans",z)
today_date()