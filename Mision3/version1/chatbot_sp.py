 # CHATBOT SUPERVISADO

# Scikit-learn
from sklearn.feature_extraction.text import CountVectorizer # Convierte texto en vector
from sklearn.naive_bayes import MultinomialNB # Analiza texto y posible respuesta, es un interprete de texto 

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

    return model, vectorizer, unique_answer

# ================================================
# Funcion predict_answer
# ================================================

def predict_answer (model, vectorizer, unique_answer, user_text) :

    # Convertir el texto a vector
    x = vectorizer.transform ( [user_text] )

    # El modelo predice la etiqueta de la respuesta correcta
    label = model.predict (x)[0]

    return unique_answer [label]

# ================================================
# PROGRAMA PRINCIPAL
# ================================================

if __name__ == "__main__":
    
    training_data = [
    ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?"),
    ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
    ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
    ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
    ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
    ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
    ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
    ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!")
    ]

    # Entrenar el modelo con la lista 
    model, vectorizer , unique_answer = build_and_train_model (training_data)

    # Mostrar un mensaje inicial al usuario
    print ("Chatbot supervisado listo, Escribe salir para terminar.\n")
    
    while True :
        
        # Pedimos una frase al usuario
        user = input ("Tu: ").strip()
        if user.lower() in {"salir", "exit", "quit"} :
            print ("Bot: !Hasta pronto¡")
            break
        response = predict_answer (model,vectorizer,unique_answer,user)
        print ("Bot: ", response)

# ================================================