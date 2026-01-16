# librerías
import re
"""
Espresiones regulares en Python
Problemas Reales 
"""
#Codigo
print("Librería cargada correctamente")
# Ejemplo1
texto="Mi Número es 12345"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")   
texto="Mi Número es 12345-985"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}") 
resultado = re.findall(r"\d+",texto)
print(f"{texto} resultado {resultado}")

#funciones
documento1 = "cc-75-055-60"


def clean_id(documento): #def para declarar funcion 
    return re.sub(r"\D","",documento)
print(clean_id(documento1))
