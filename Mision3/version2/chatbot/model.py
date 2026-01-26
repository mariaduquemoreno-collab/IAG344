 # CHATBOT SUPERVISADO

import os # Hace la conexion entre rutas
import pickle #Guarda rutas

# Scikit-learn
from sklearn.feature_extraction.text import CountVectorizer # Convierte texto en vector
from sklearn.naive_bayes import MultinomialNB # Analiza texto y posible respuesta, es un interprete de texto 

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH = os.path.join (MODEL_DIR, "vectorizer.pkl")
ANSWER_PATH = os.path.join (MODEL_DIR, "answers.pkl")

# ================================================
# Funcion build_and_train_model
# Funcion de entrenamiento: Preguntas y respuestas
# ================================================

def build_and_train_model(train_pairs): # train_pairs: lista de pares (Pregunta, Respuesta)
    # Ejemplo [("Hola", "!Hola¡")], ("Adios", !Hasta Luego¡)
    
    # Separamos las preguntas y respuestas en dos listas
    questions = [q for q, _ in train_pairs] # Lista de Preguntas
    answers = [a for _, a in train_pairs] # Lista de Respuestas

    # Creamos el vectorizadp, que traduce traducira el texto a numeros
    vectorizer = CountVectorizer()

    #Entrenamiento
    x = vectorizer.fit_transform (questions) # fit_transform Transforma varios textos

    # Obtenemos una lista de respuestas unicas
    unique_answer = sorted(set(answers))

    #Crear el diccionario con las etiquetas
    answer_to_label = { a: i for i, a in enumerate (unique_answer)}

    # Creamos una lista
    y = [answer_to_label [a] for a in answers]

    # Modelo clasificacion de texto
    model = MultinomialNB()

    # Entrenar el modelo
    model.fit (x,y)

    #Crear carpeta para guardar el model si no existe
    os.makedirs (MODEL_DIR, exist_ok=True)

    # Guardar los objetos entrenados
    with open (MODEL_PATH, "wb") as f : #Manejo y apertura de archivos, wb para abrir archivos binarios
        pickle.dump (model, f) 
    with open (VECTORIZER_PATH, "wb") as f :
        pickle.dump (vectorizer, f)
    with open (ANSWER_PATH, "wb") as f :
        pickle.dump (unique_answer, f)
    print ("🆗 Modelo entrenado correctamente")
    
    return model, vectorizer, unique_answer

# ================================================
# Funcion load_model
# ================================================

def load_model () :
    """
    Carga el modelo, el vectorizado y las respuestas si existen 
    """
    if (
        os.path.exists (MODEL_PATH)
        and os.path.exists (VECTORIZER_PATH)
        and os.path.exists (ANSWER_PATH) 
    ):
        with open (MODEL_PATH, "rb") as f:
            model = pickle.load (f)
        with open (VECTORIZER_PATH, "rb") as f:
            vectorizer = pickle.load (f)
        with open (ANSWER_PATH, "rb") as f:
            unique_answer = pickle.load (f)
        print ("📁 Modelo cargado desde disco.")

        return model, vectorizer, unique_answer
    
    else :
        print ("⚠ No hay modelo guardado, será necesario entrenarlo")
        return None, None, None

# ================================================
# Funcion predict_answer
# ================================================

def predict_answer (model, vectorizer, unique_answer, user_text) :

    # Convertir el texto a vector
    x = vectorizer.transform ( [user_text] )

    # El modelo predice la etiqueta de la respuesta correcta
    label = model.predict (x)[0]

    return unique_answer [label]
