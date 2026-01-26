# Librerias

import re

""" (Tres comillas para comentar varias lineas, # para comentar una sola linea)
Expresiones reguares en Python
Problemas reales
"""
# Codigo

print ( "Libreria cargada correctamente" )

#Ejemplo 1
texto = "Mi numero es 12345" #Decalracion de variables, no es necario declarar el tipo de variable string o int
resultado = re.search(r"\d+",texto) #Busca con el comando  en este caso solo los digitos y los almacena
print(resultado.group()) #Imprime el conjunto de todos los caracteres encontrados y almacenados
print (f"{texto} Resultado {resultado.group()}")
texto = "Mi numero es 12345-985"
resultado = re.search(r"\d+",texto)
print (f"{texto} Resultado {resultado.group()}") #Con la f y {} se puede remplazar la concatenzacion  regular para juntar texto y variables
resultado = re.findall(r"\d+",texto) #Findall busca y pone en una lista todos los elementos que se le indican
print ( f"{texto} Resultado {resultado}")#Si el print es de un findall no se le necesita poner .group

# Funciones
documento1 = "cc-75-055-60"

def clean_id(documento): #Declaracion de una funcion
    return re.sub(r"\D","",documento)#re.sub coje todo aquello que se le daen parametro y los reemplaza, ademas agrupa lo restante
print (clean_id(documento1))