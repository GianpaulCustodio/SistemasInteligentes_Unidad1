#Librería para leer txt utf-8
import codecs
#Librería para Polaridad
from textblob import TextBlob

resumenTxt=codecs.open("MensajePrueba.txt","r")
lectura=resumenTxt.read()
t=TextBlob(lectura)
ten = t.translate(to="en")
polaridadLista = list(ten.sentiment)
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