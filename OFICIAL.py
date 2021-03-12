#Librería PDF -> HTML
import fitz
#Librería para Realizar Resumen 
import bs4 as bs  
import urllib.request  
import re
import nltk
import bs4
import urllib.request
import requests
from bs4 import BeautifulSoup
import urllib.request
from inscriptis import get_text
from googletrans import Translator
from pdfminer.high_level import extract_text
nltk.download('punkt')
nltk.download('stopwords')

def PdfToHTML():
    #Insertamos el PDF(1)
    pdf = "Lectura1.pdf"
    documento = fitz.open(pdf)
    pagina = documento.loadPage(0)
    doc = fitz.open(pdf)
    salida = open(pdf+".html","wb")
    #salida = open(pdf+".txt","wb") -> .txt(1)
    for pagina in doc:
        #texto = pagina.getText().encode("utf8") .txt(2)
        texto = pagina.getText("html").encode("utf8")
        salida.write(texto)
        salida.write(b"\n--------------------\n")
    salida.close()
    Resumen()  

def Resumen():
    #Insertamos el PDF(2)
    pdfTohtml = extract_text("Lectura1.pdf")
    articulo_texto = pdfTohtml
    articulo_texto = articulo_texto.replace("[ edit ]", "")
    print ("#########################")
    print ("##### R E S U M E N #####")
    print ("#########################")

    from nltk import word_tokenize,sent_tokenize
    # Elimina palabras vacías, espacios extras
    articulo_texto = re.sub(r'\[[0-9]*\]', ' ', articulo_texto)  
    articulo_texto = re.sub(r'\s+', ' ', articulo_texto)  

    formatear_articulo = re.sub('[^a-zA-Z]', ' ', articulo_texto )  
    formatear_articulo = re.sub(r'\s+', ' ', formatear_articulo)  

    #EN ESTA PARTE HACE LA TOKENIZACION 
    lista_palabras = nltk.sent_tokenize(articulo_texto)  

    #EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
    stopwords = nltk.corpus.stopwords.words('english')

    frecuencia_palabras = {}  
    for word in nltk.word_tokenize(formatear_articulo):  
        if word not in stopwords:
            if word not in frecuencia_palabras.keys():
                frecuencia_palabras[word] = 1
            else:
                frecuencia_palabras[word] += 1

    #
    max_frecuencia = max(frecuencia_palabras.values())

    for word in frecuencia_palabras.keys():  
        frecuencia_palabras[word] = (frecuencia_palabras[word]/max_frecuencia)

    #CALCULA LAS FRASES QUE MÁS SE REPITEN
    max_oracion = {}  
    for sent in lista_palabras:  
        for word in nltk.word_tokenize(sent.lower()):
            if word in frecuencia_palabras.keys():
                if len(sent.split(' ')) < 90:
                    if sent not in max_oracion.keys():
                        max_oracion[sent] = frecuencia_palabras[word]
                    else:
                        max_oracion[sent] += frecuencia_palabras[word]

    #REALIZA EL RESUMEN CON LAS MEJORES FRASES
    import heapq  
    resumen_oracion = heapq.nlargest(7, max_oracion, key=max_oracion.get)

    resumen = ' '.join(resumen_oracion)  
    print(resumen)  

    #Traducción
    translator = Translator()
    translate = translator.translate(resumen, src="es", dest="es")

    #Guardar en .txt
    resumenpdf = open ("Resumenn.txt","w")
    resumenpdf.write("Resumen del texto:\n" + translate.text)
    resumenpdf.close()
    

PdfToHTML()