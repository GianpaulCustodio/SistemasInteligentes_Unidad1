#Librería para leer txt utf-8
import codecs
#Librería para Polaridad
from textblob import TextBlob

#Lectura de txt
# resumenTxt=codecs.open("oli.txt","r","utf-8")
# lectura=resumenTxt.read()
# resumenTxt.close()
# print(lectura)

# resumenTxt=codecs.open("Resumen.txt","r")
# lectura=resumenTxt.read()
# t=TextBlob(lectura)
# ten = t.translate(to="en")
#print(ten.sentiment,"\n")

resumenTxt=codecs.open("oli.txt","r")
lectura=resumenTxt.read()
t=TextBlob(lectura)
ten = t.translate(to="en")

polaridadLista = list(ten.sentiment)
#polaridadFinal = " ".join(polaridadLista)
polaridad = open ("Polaridad.txt","w")
polaridad.write("POLARIDAD:" + str(polaridadLista[0])+"\nSUBJETIVIDAD: " + str(polaridadLista[1]))
polaridad.close()