#Librería para leer txt utf-8
import codecs
#Librería para Polaridad
from textblob import TextBlob
from googletrans import Translator

# resumenTxt=codecs.open("MensajePrueba.txt","r")
# lectura=resumenTxt.read()
# t=TextBlob(lectura)
# ten = t.translate(to="en")
# polaridadLista = list(ten.sentiment)
# polaridad = open ("Polaridad.txt","w")
# if polaridadLista[0]<0:
#     polaridad.write("OPINIÓN NEGATIVA\n\n")
#     polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1])+"\n")
# elif polaridadLista[0]==0:
#     polaridad.write("OPINIÓN NEUTRAL\n\n")
#     polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1])+"\n")
# elif polaridadLista[0]>0 and polaridadLista[0] <=1:
#     polaridad.write("OPINIÓN POSITIVA\n\n")
#     polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1])+"\n")
# polaridad.close()



#Opcion B
#t=TextBlob("La comida está deliciosa").translate(from_lang="es",to='en').sentiment
# print(t)

def Funcionactm():
    translator = Translator()
    lista="La comida está deliciosa"
    translate = translator.translate(lista, src="en", dest="es")
    aux=translate.text
    hola=str(lista)
    aux2=TextBlob(hola).sentiment
    print(aux2)
    #aux=TextBlob(translaate).sentiment
    #print(translaate.text)

Funcionactm()