#Importar Librerias
import random
import time

#COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Contador de Trivia
iniciar_trivia = True
intentos = 0

while iniciar_trivia == True:
    intentos+=1
    #Agregando Título
    #Contexto de la Trivia
    print(BLUE+"\n\t\t\t\t\t\t\t\t**Trivia de Videojuegos**"+RESET)
    print(YELLOW+"Se pondrán a prueba tus conocimientos"+RESET)
    #Solicitando nombre
    nombre = input(MAGENTA+"Ingresa tu nombre: "+RESET)


    #PUNTAJES INICIALES DE LAS 3 PREGUNTAS
    puntajeA = 0
    puntajeB = 0
    puntajeTotal = random.randint(0,20)
    print(GREEN + "Hola " + BLACK + f"{nombre.capitalize()}" + GREEN + " al comenzar obtendrás un puntaje aleatorio que va de" + BLACK +" 0 a 20," + GREEN + " Suerte !!!"+RESET)
    print(RED + "Tu puntaje inicial es "+ BLACK + f"{puntajeTotal}"+RESET)

    #Instrucciones de la trivia
    print(BLACK+f"{nombre.capitalize()} responde las siguientes preguntas y presiona" + RED + " *ENTER* "+ RESET+ BLACK+"para enviar tu respuesta:\n"+RESET)

    for pre in range(5 , 0, -1):
        print(YELLOW+f"Empezamos en {pre}"+RESET)
        time.sleep(1)

    #Pregunta 01
    print(GREEN + "\n1)"+ BLACK + "¿En qué año salió al mercado la primera consola?\n"+RESET)
    print("\ta) 1969")
    print("\tb) 1970")
    print("\tc) 1971")
    print("\td) 1972")
    print("\te) 1968\n")

    #Almacenando respuesta 01
    r_p1 = input(BLACK+"Tu Respuesta: "+RESET)
    while r_p1 not in ("a","b","c","d","e","1969","1970","1971","1972","1968"):
        r_p1 = input(YELLOW+"Respuesta no válida, vuelve a ingresar una respuesta: "+RESET)

    #Evaluando Respuesta y Resultado p01
    if r_p1 == "1972" or r_p1 == "d":
        #AGREGANDO PUNTAJE RANDOM DE 0 A 8
        puntajeA = random.randint(10,20)
    #IMPRIMIENDO RESPUESTA CORRECTA Y PUNTAJE
        print(GREEN+f"\n{nombre.capitalize()} tu respuesta es correcta, has obtenido {puntajeA} puntos!!!"+RESET)
        puntajeTotal+=puntajeA
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p1 == "1969" or r_p1 == "a":
        puntajeA = random.randint(-2,0)
        print(RED+f"\n{nombre.capitalize()} tu respuesta es incorrecta!"+RESET)
        puntajeTotal+=puntajeA
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p1 == "1970" or r_p1 == "b":
        puntajeA = random.randint(-2,0)
        print(RED+f"\n{nombre.capitalize()} tu respuesta es incorrecta!"+RESET)
        puntajeTotal+=puntajeA
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p1 == "1971" or r_p1 == "c":
        puntajeA = random.randint(-2,0)
        print(RED+f"\n{nombre.capitalize()} tu respuesta es incorrecta!"+RESET)
        puntajeTotal+=puntajeA
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p1 == "1968" or r_p1 == "e":
        puntajeA = random.randint(-2,0)
        print(RED+f"\n{nombre.capitalize()} tu respuesta es incorrecta!"+RESET)
        puntajeTotal+=puntajeA
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)

    #PREGUNTA 2
    print(BLACK+ "\n2) ¿Quién es el fundador de la tienda de Videojuegos Steam?\n" + RESET)
    print("\ta) Tim Sweeney")
    print("\tb) Gabe Newell")
    print("\tc) Michael Morhaime")
    print("\td) Frank Pearce")
    print("\te) Yves Guillemot\n")

    #Almacenando respuesta 02
    r_p2 = input(BLACK + "Tu Respuesta: " + RESET)
    while r_p2 not in ("a","b","c","d","e","Tim Sweeney","Gabe Newell","Michael Morhaime","Frank Pearce","Yves Guillemot"):
        r_p2 = input(YELLOW+"Respuesta no válida, vuelve a ingresar una respuesta: "+RESET)

    #Evaluando Respuesta y Resultado p02
    if r_p2 == "Gabe Newell" or r_p2 == "b":
        puntajeB += random.randint(6,10)
        print(GREEN + f"\n{nombre.capitalize()} tu respuesta es correcta!, has obtenido " + BLACK + f"{puntajeB} "+ GREEN +"puntos" + RESET)
        print(BLUE +"Felicidades tu puntaje se multiplicada por 2, ya que acertaste!!!"+ RESET)
        puntajeTotal+=(2*puntajeB)
        print(MAGENTA +f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p2 == "Tim Sweeney" or r_p2 == "a":
        puntajeB = random.randint(0,2)
        print(RED + f"\n{nombre.capitalize()} tu respuesta es incorrecta, se te descontará {puntajeB} puntos"+ RESET)
        print(RED+ "Ya que fallaste se te descontarán otros 5 puntos" + RESET)
        puntajeTotal-=(puntajeB+5)
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p2 == "Michael Morhaime" or r_p2 == "c":
        puntajeB = random.randint(-2,0)
        print(RED+f"\n{nombre.capitalize()} tu respuesta es incorrecta, se te descontara {abs(puntajeB)} puntos "+RESET)
        puntajeTotal+=(puntajeB)
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p2 == "Frank Pearce" or r_p2 == "d":
        puntajeB = random.randint(-2,0)
        print(RED+f"\n{nombre.capitalize()} tu respuesta es incorrecta, se te descontara {abs(puntajeB)} puntos "+RESET)
        puntajeTotal+=puntajeB
        print(MAGENTA+f"Tu puntaje total es: {puntajeTotal}"+RESET)
    elif r_p2 == "Yves Guillemot" or r_p2 == "e":
        puntajeB = random.randint(-2,0)
        print(RED + f"\n{nombre.capitalize()} tu respuesta es incorrecta, se te descontara {abs(puntajeB)}" +RESET)
        puntajeTotal+=puntajeB
        print(RED+ "Error gravísimo, tu puntaje total se reduce a la mitad" + RESET)
        puntajeTotal/=2
        print(MAGENTA+f"Tu puntaje total es: {int(puntajeTotal)}"+RESET)

    print(RED+ "\nOjo:No te aseguramos tener un puntaje mayor"+RESET)
    RuleR = input("Escribe 'si' para obtener un puntaje por medio de una ruleta aleatoria: ").lower()
    if RuleR != "si":
        print(BLUE +f"\nMuchas gracias {nombre.capitalize()} por participar en esta trivia tu nueva puntuacion total es {puntajeTotal}"+RESET)
    else:
        for int in range(10,0,-1):
            Vran = random.randint(0,20)
            print(YELLOW+ f"Tu nueva puntuación es {Vran}"+RESET)
            time.sleep(0.8)
        print(BLUE+f"\nMuchas gracias {nombre.capitalize()} por participar en esta trivia tu puntuacion total es {Vran}"+RESET)

    print(BLACK+"\n¿Deseas intentar nuevamente la trivia?"+RESET)
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

    if repetir_trivia != "si":
        print(BLUE+f"Espero lo hayas pasado genial {nombre}, Suerte y Exitos!!!"+RESET)
        iniciar_trivia = False