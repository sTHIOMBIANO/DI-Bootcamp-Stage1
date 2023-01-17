from translate import Translator

dict={}


french_words=["Bonjour","Au revoir","Bienvenue","A bientot"]
i=0
while i < len(french_words):
    elem=french_words[i]
    translator=Translator(to_lang="en", from_lang="fr")
    elem=translator.translate(elem)
    dict[french_words[i]]=elem
    i+=1

print(dict)

