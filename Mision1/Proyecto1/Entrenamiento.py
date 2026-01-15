#librerias 
import re
"""
comillas para comentar en varias lineas 
"""
#codigo
print("libreria cargada correctamente") # print funciona como el sout 

#ejemplo
texto="mi Numero es 12345" #igual para variables "comillas para cadenas de texto o string"
resultado=re.search(r"/d+",texto) #busca los numeros que se encuentren en la variable texto
print(resultado.group()) #muestra el resultado de la busqueda 

# [] listas {} diccionario 