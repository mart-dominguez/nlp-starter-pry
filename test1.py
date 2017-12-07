from nltk import word_tokenize
from nltk import sent_tokenize
import io
from  utils.readpdf import joke
'''
from PyPDF2 import PdfFileReader
with open("test.pdf",'rb') as f:
    if f:
        ipdf = PdfFileReader(f)
        textpdf = [p.extractText() for p in ipdf.pages]


mifile = io.open("test.txt", 'w', encoding='utf8') #open("test.txt","w")

for item in textpdf:
    mifile.write(item)

mifile.close()
'''

archivo = "test.txt"
f1 = io.open(archivo, 'rU', encoding='utf-8')
#file1 = open(archivo,"r")
text = f1.read()
print(text[:45])

# obtengo los tokens
tokens = word_tokenize(text)
print(type(tokens))
print(len(tokens))
print(tokens[:10])

oraciones = sent_tokenize(text)
print(len(oraciones))
print(oraciones[:2])