import re 
def clean_id(value):
    #elimina caracteres no numericos de un documento
    if value is None:
        return ""
    return re.sub(r'\D','',str(value))