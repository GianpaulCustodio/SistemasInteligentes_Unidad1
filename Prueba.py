# with open ('D:/Google Drive/Google Drive/UEM/2021-1/Sistemas Inteligentes y Representación del Conocimiento/Unidad1/oli.txt','r',encoding="utf-8") as texto:
#     for linea in texto:
#         print(linea)

from io import open

archivo_texto=open("oliii.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)



























# import bs4 as bs  
# import urllib.request  
# import re
# import nltk
# import bs4
# import urllib.request
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
# from inscriptis import get_text
# from googletrans import Translator
# nltk.download('punkt')
# nltk.download('stopwords')
# #scrapea articulo de wikipedia
# enlace = "file:///D:/Google%20Drive/Google%20Drive/UEM/2021-1/Sistemas%20Inteligentes%20y%20Representaci%C3%B3n%20del%20Conocimiento/Unidad1/Unidad1.pdf.html"
# html = urllib.request.urlopen(enlace).read().decode('utf-8')
# text = get_text(html)
# article_text = text
# article_text = article_text.replace("[ edit ]", "")
# print ("#########################")
# print ("##### R E S U M E N #####")
# print ("#########################")
 
# from nltk import word_tokenize,sent_tokenize
# # Removing Square Brackets and Extra Spaces
# article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
# article_text = re.sub(r'\s+', ' ', article_text)  
 
# formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
# formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  
# #nltk.download()
# #EN ESTA PARTE HACE LA TOKENIZACION 
# sentence_list = nltk.sent_tokenize(article_text)  
 
# #EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
# stopwords = nltk.corpus.stopwords.words('english')
 
# word_frequencies = {}  
# for word in nltk.word_tokenize(formatted_article_text):  
#     if word not in stopwords:
#         if word not in word_frequencies.keys():
#             word_frequencies[word] = 1
#         else:
#             word_frequencies[word] += 1
 
# #
# maximum_frequncy = max(word_frequencies.values())
 
# for word in word_frequencies.keys():  
#     word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
 
# #CALCULA LAS FRASES QUE MÁS SE REPITEN
# sentence_scores = {}  
# for sent in sentence_list:  
#     for word in nltk.word_tokenize(sent.lower()):
#         if word in word_frequencies.keys():
#             if len(sent.split(' ')) < 30:
#                 if sent not in sentence_scores.keys():
#                     sentence_scores[sent] = word_frequencies[word]
#                 else:
#                     sentence_scores[sent] += word_frequencies[word]
 
# #REALIZA EL RESUMEN CON LAS MEJORES FRASES
# import heapq  
# summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
 
# summary = ' '.join(summary_sentences)  
# print(summary)  
 
# ###
# #traducir:
# ################
# translator = Translator()
# translate = translator.translate(summary, src="es", dest="es")
# print(translate.text)
