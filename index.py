import openai

openai.api_key = "" # <--- colocar KEY de OpenAI.
initialPrompt = """hace de cuenta que sos un analizador de sentimientos. yo te paso sentimientos y vos analizas
                   el sentimiento de los mensaje y me das una respuesta con al menos 1 caracter y un máximo de 4 caracteres
                   SOLO RESPUESTAS NUMÉRICAS, -1 es negatividad máxima, 0 es neutral y 1 es positivo. (podes usar valores flotantes).""" #prompt del ia.

messages = [
    {"role": "system", "content": initialPrompt}
]

class AnalizadorDeSentimientos: # Creando una Clase para detectar todos los sentimientos
    def analizar_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m"+'negativo'+"\x1b[0;37m" # detectar algo negativo.
        elif polaridad > -0.3 and polaridad < 0:
            return "\x1b[1;31m"+'algo negativo'+"\x1b[0;37m" # detectar que es ALGO NEGATIVO.
        elif polaridad == 0:
            return "\x1b[1;33m"+'neutral'+"\x1b[0;37m" # detectar que es NEUTRAL (o algo NORMAL.)
        elif polaridad > 0 and polaridad <= 0.3:
            return "\x1b[1;33m"+'algo positivo' # detectar que es ALGO POSITIVO.
        elif polaridad > 0.3 and polaridad <= 0.6:
            return "\x1b[1;32m"+'positivo' # detectar que es algo que es positivo
        elif polaridad > 0.6 and polaridad <= 0.9:
            return "\x1b[1;32m"+'muy positivo' # detectar algo que es muy positivo
        elif polaridad > 0.9 and polaridad <= 1:
            return "\x1b[1;32m"+'muy muy positivo' # detectar que algo es muy muy positivo
        else :
            return "\x1b[1;31m"+'muy negativo'+"\x1b[0;37m"


analizador = AnalizadorDeSentimientos()


while True:
    
    userPrompt = input("\x1b[1;33m"+"\Dime algo: "+"\x1b[0;37m") # el usuario NECESITA colocar una oración/frase
    messages.append({"role": "user", "content": userPrompt})
    
    completion = openai.ChatCompletion.create( #creación del IA, ad: PONIENDO EL MODELO, LOS MENSAJES Y EL MAX DEL TOKEN.
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1200
    )

    # Agregar respuesta del modelo a la conver 
    messages.append({
        "role": "assistant",
        "content": completion.choices[0].message['content']
    })
    
    sentimiento = analizador.analizar_sentimiento(float(completion.choices[0].message['content'])) # Acá anilaza la oración/frase.

    print(sentimiento) # acá muestra todo

    
