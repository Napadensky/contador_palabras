#IMPORTACION
import sys


#FUNCION
def conteo(txt):
    try:
        open_txt = open(txt)
    except:
        sys.exit(f'El archivo {txt} no se encontro.')
    words = open_txt.read()
    quitar = '.,":;'
    dic_words = dict()
    for caracter in quitar:
        words = words.replace(caracter, '')

    words = words.split(' ')

    for palabra in words:
        if palabra in dic_words:
            dic_words[palabra] += 1
        else:
            dic_words[palabra] = 1
    for palabra in words:
        repeat = dic_words[palabra]
        print(f'> {palabra}   :{repeat}')


print('\n\n===================================')
print('============  INICIO  =============')
print('===================================')
archivo = input('\nAgrega el nombre de un txt que este en la raiz de este programa: ')
conteo(archivo)
print('\n\n===================================')
print('=============  FIN  ===============')
print('===================================')