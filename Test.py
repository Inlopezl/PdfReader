from ast import While
import functools
from xml.dom.minidom import Element
import pdfplumber
import os

start = 0
end = 0

#nopermitidos = '(/&$#"!!'


cantArchivos=14
ruta=''

for y in range(cantArchivos):
    ''' ruta del archivo '''
    ruta = './Mendoza/mndz' + '-' + str(y+1) + '.pdf'

    ''' inicio de funcion de lectura '''
    with pdfplumber.open(ruta) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        # texto separado por palabras
        textSplitted = text.split()
        name=[]
            
        for i in textSplitted: 
            
            if i == 'corresponda)':
                start = textSplitted.index(i)
            #if  'corresponda)' in i:
            #    start = textSplitted.index(i)
            pass
            if  'Mendoza' in i and end != '3':
                end += 1
            pass

            if start > 0 and end < 3:
                if textSplitted.index(i) != start and not 'de' in i  :
                    name.append(textSplitted.index(i))
                pass

    print(name)
    # os.rename(r'./'+ ruta,r'./'+  ts[a[0]])
