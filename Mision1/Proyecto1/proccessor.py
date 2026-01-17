import re 
def clean_id(value):
    # funcion clean id
    #elimina caracteres no numericos de un documento
    if value is None:
        return ""
    return re.sub(r'\D','',str(value))

#funcion merge_name
#un nombre y apellido en un solo campo
def merge_name(name,lastname):
    if name is None:
        name = ""
    if lastname is None:
        lastname = ""
    return f"{name}{lastname}" .strip()

from proccessor import clean_id,merge_name
def test_clean_id():
    assert clean_id("cc-75.087.345")

 


