from textblob import TextBlob
from googletrans import Translator
import codecs
# def Funcionactm():
#     translator = Translator()
#     lista="La comida está deliciosa"
#     translate = translator.translate(lista, src="es", dest="en")
#     aux=translate.text
#     aux2=TextBlob(aux).sentiment
#     print(aux2)
    #aux=TextBlob(translaate).sentiment
    #print(translaate.text)

def Polaridad():
    translator = Translator()
    resumenTxt = codecs.open("oli.txt","r")
    lectura=resumenTxt.read()
    translate = translator.translate(lectura, src="es", dest="en")
    t=TextBlob(translate.text)
    t = t.sentiment
    #print(list(t))
    polaridadLista = list(t)
    polaridad = open ("Polaridad.txt","w")
    if polaridadLista[0]<0:
        polaridad.write("OPINIÓN NEGATIVA\n\n")
        polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1])+"\n")
    elif polaridadLista[0]==0:
        polaridad.write("OPINIÓN NEUTRAL\n\n")
        polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1])+"\n")
    elif polaridadLista[0]>0 and polaridadLista[0] <=1:
        polaridad.write("OPINIÓN POSITIVA\n\n")
        polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1])+"\n")
    polaridad.close()

Polaridad()