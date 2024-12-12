import requests
import random
import os
import time

# Me borras cuando yo quiera
def os_clear():
    os.system('cls')

# Obtenme preguntas een opendtb
def obtenme_preguntas(cantidad=15):
    url = f"https://opentdb.com/api.php?amount={cantidad}&type=multiple"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos['results']
    except Exception as e:
        print(f"Error al obtener preguntas: {e}")
        return []

def muestrame_pregunta(pregunta):
    print(f"\n{pregunta['question']}")
    opciones = pregunta['incorrect_answers'] + [pregunta['correct_answer']]
    random.shuffle(opciones)

    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    return opciones

def juego_millonario():
    print("Bienvenido a Quién quiere ser millonario!")
    print("")
    nombre = input("Por favor, introduce tu nombre: ")
    print(f"Hola {nombre}, estas preparado? Comienza el juego\n")
    print("---------------------------------------")
    #Importante
    preguntas = obtenme_preguntas()
    puntos = 0
    

    # Lista de comodines
    comodines = {
        ##'50%': True,
        'saltar': True,
        ##'publico': True


    }

    for i, pregunta in enumerate(preguntas):
        print(f"Pregunta {i + 1}: (Puntuación: {puntos + 1})")
        opciones = muestrame_pregunta(pregunta)


        if any(comodines.values()):
            print("Comodines disponibles:")
            for comodin, disponible in comodines.items():
                if disponible:
                    print(f"- {comodin}")
        print("\nSi quieres plantarte y terminar el juego, escribe salir.")

        respuesta_usuario = input("Tu respuesta (1-4) o escribe el comodín: ").lower()


        #if respuesta_usuario == '50%' and comodines['50%']:
         #   comodines['50%'] = False
          #  opciones_filtro = random.sample([pregunta['correct_answer']] + random.sample(pregunta['incorrect_answers'], 1), 2)

           # opciones = opciones_filtro
            #random.shuffle(opciones)


            #print("\nAquí tienes el resultado de tu comodín:")
            #for i, opcion in enumerate(opciones):
             #   print(f"{i + 1}. {opcion}")

            #respuesta_usuario = input("Tu respuesta (1-2): ").lower() 

        if respuesta_usuario == 'salir':
            os_clear()
            print("Es un placer que hayas jugado a nuestro juego.\n")
            print(f"Resultado: {puntos}\n")
            time.sleep(5)
            break

        elif respuesta_usuario == 'saltar' and comodines['saltar']:
            comodines['saltar'] = False
            print("Has usado el comodín de saltar. Pasemos a la siguiente pregunta, estate preparado, no tienes más oportunidades.\n")
            time.sleep(5)
            os_clear()
            continue


        #if respuesta_usuario == 'publico' and comodines['publico']:
         #   comodines['público'] = False
          #  estadisticas = {opcion: random.randint(0, 100) for opcion in opciones}
           # estadisticas[pregunta['correct_answer']] += random.randint(10, 30)
            #total = sum(estadisticas.values())


            #for opcion in estadisticas:
             #   estadisticas[opcion] = int((estadisticas[opcion] / total) * 100)
            #print("\nVeamos las votaciones del público: ")
            #time.sleep(5)
            
            #for opcion, porcentaje in estadisticas.items():
             #   print(f"{opcion}: {porcentaje}%")
            #respuesta_usuario = input("Tu respuesta (1-4): ").lower()


        try:
            indice_respuesta = int(respuesta_usuario) - 1
            if opciones[indice_respuesta] == pregunta['correct_answer']:
                print("Correcto!")
                print("Pasemos a la siguiente pregunta")
                time.sleep(5)
                os_clear()
                puntos += 1
                if puntos == 15:
                    print("Has ganado, eres el mejor macho")
                    break
            else:
                print(f"Incorrecto. La respuesta era: {pregunta['correct_answer']}")
                time.sleep(5)
                os_clear()
                print(f"---------------Resultados finales----------------")
                print(f"---------------PUNTOS: {puntos}----------------")
                puntos == 0
                time.sleep(5)
                os_clear()
                break
        except (ValueError, IndexError):
            print("Respuesta incorrecta. Fin del juego.")
            break

    print(f"\nJuego terminado. {nombre}")

juego_millonario()
