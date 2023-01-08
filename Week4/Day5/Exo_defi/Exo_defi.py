


phrase="je,suis,en,train,de,traiter,les,exercices,du,defi"
def ordre_mot(phrase):
    var=phrase.split(",")
    var1=sorted(var)
    var2=",".join(var1)
    print(var2)


ordre_mot(phrase)