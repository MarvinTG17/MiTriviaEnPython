import random
import time

#Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
a = 1
b = 2

#Titulo
print(BLUE+'BIEVENIDO A MI PRIMERA TRIVIA CON PYTHON.\n')

#tiempo
time.sleep(1)

#ciclo con tiempo
for variable in range (5,0,-1):
  print (RED,variable)
  time.sleep(1)
  
#Pedir nombre del usuario
nombre = input(YELLOW+"\nIngresa tu nombre: ")
  
  #Condicion si el nombre es vacio o menor a 2 caracteres
while nombre == "" or len(nombre) <= 2:
  print(RED+"\nError, el nombre esta vacio o debe tener mas de 2 letras.\n")
  nombre = input(YELLOW+"Por favor, ingresa tu nombre: ")
  
#Tiempo
time.sleep(1)

#ciclo de intentos para la trivia
iniciar_trivia = True
intentos = 0

while iniciar_trivia == True:
  intentos += 1
  print("\nIntento numero: ",intentos)

  #tiempo
  time.sleep(1)

  #Bienvenida
  print(YELLOW+"\nHola "+BLUE,nombre,YELLOW+", responde las siguientes preguntas escribiendo la alternativa y presionando 'Enter' para enviar tu respuesta.\n")
  
  #Tiempo
  time.sleep(5)
  
  #Explicacion de los puntajes
  print("Cada pregunta respondida correctamente, ganaras 10 puntos y cada incorrecta te restara 5 puntos.\n")
  
  #Tiempo
  time.sleep(4.5)
  
  #Puntos
  puntos = random.randint(0,10)
  print("Comenzaras con "+BLUE,puntos,YELLOW+"puntos.\n")
  
  #Tiempo
  time.sleep(2)
  
  #ciclo con tiempo
  for variable in range (5,0,-1):
    print (RED,variable)
    time.sleep(1)
  
  # Pregunta 1
  print(BLUE+"\nPregunta N°1: ¿Año de la independencia del Peru?"+RESET)
  print(CYAN+"a)"+RESET+" 1918")
  print(CYAN+"b)"+RESET+" 1921")
  print(CYAN+"c)"+RESET+" 1922")
  print(CYAN+"d)"+RESET+" 1919")
  
  respuesta_1 = input("\nTu respuesta: ")
  
  #Tiempo
  time.sleep(1)
  
  while respuesta_1 not in ("a", "b", "c", "d", "m"):
    respuesta_1 = input(RED+"\nNo es una de las alternativas, volver a intentarlo.\n\n"+RESET+"Ingresa nuevamente tu respuesta:")
    #Tiempo
    time.sleep(1)
  
  
  if respuesta_1 == "b":
    puntos += 10
    print(GREEN+"\nRespuesta correcta.\n")
  elif respuesta_1 == "m":
    puntos += 20
    print(MAGENTA+"\nEncontraste la alternativa secreta, ganastes 20 puntos.\n")
  else:
    puntos -= 5
    print(RED+"\nRespuesta incorrecta.\n")
  
  #Tiempo
  time.sleep(1)
  
  #puntaje
  print(CYAN+"Tienes ", puntos, " puntos.\n")
  
  #Tiempo
  time.sleep(1)
  
  # Pregunta 2
  print(BLUE+"Pregunta N°2: ¿Cual cultura realizaba las trepanaciones craneanas?")
  print(CYAN+"a)"+RESET+" Nazca")
  print(CYAN+"b)"+RESET+" Mochica")
  print(CYAN+"c)"+RESET+" Chavin")
  print(CYAN+"d)"+RESET+" Paracas")
  
  respuesta_2 = input("\nTu respuesta: ")
  
  #Tiempo
  time.sleep(1)
  
  while respuesta_2 not in ("a", "b", "c", "d", "r"):
    respuesta_2 = input(RED+"\nNo es una de las alternativas, volver a intentarlo.\n\n"+RESET+"Ingresa nuevamente tu respuesta:")
    #Tiempo
    time.sleep(1)
  
  if respuesta_2 == "d":
    puntos += 10
    print(GREEN+"\nRespuesta correcta.\n")
  elif respuesta_2 == "r":
    puntos += 20
    print(MAGENTA+"\nEncontraste la alternativa secreta, ganastes 20 puntos.\n")
  else:
    puntos -= 5
    print(RED+"\nRespuesta incorrecta.\n")
  
  #Tiempo
  time.sleep(1)
  
  #puntaje
  print(CYAN+"Tienes ", puntos, " puntos.\n")
  
  #Tiempo
  time.sleep(2)
  
  # Pregunta 3
  print(BLUE+"Pregunta N°3: ¿Cuales son los suyos del Tahuantinsuyo?")
  print(CYAN+"a)"+RESET+" Collasuyo, Chinchaysuyo, Antisuyo, Contasuyo.")
  print(CYAN+"b)"+RESET+" Chinllasuyo, Cochaysuyo, Antisuyo, Contisuyo.")
  print(CYAN+"c)"+RESET+" Collasuyo, Chinchaysuyo, Antisuyo, Contisuyo.")
  print(CYAN+"d)"+RESET+" Collasuyo, Chinchasuyo, Antisuyo, Contisuyo.")
  
  respuesta_3 = input("\nTu respuesta: ")
  
  #Tiempo
  time.sleep(1)
  
  while respuesta_3 not in ("a", "b", "c", "d", "v"):
    respuesta_3 = input(RED+"\nNo es una de las alternativas, volver a intentarlo.\n\n"+RESET+"Ingresa nuevamente tu respuesta:")
    #Tiempo
    time.sleep(1)
  
  if respuesta_3 == "c":
    puntos += 10
    print(GREEN+"\nRespuesta correcta.\n")
  elif respuesta_3 == "v":
    puntos += 20
    print(MAGENTA+"\nEncontraste la alternativa secreta, ganastes 20 puntos.\n")
  else:
    puntos -= 5
    print(RED+"\nRespuesta incorrecta.\n")
  
  #Tiempo
  time.sleep(1)
  
  #puntaje
  print(CYAN+"Tienes ", puntos, " puntos.\n")
  
  #Tiempo
  time.sleep(1)
  
  # Pregunta 4
  print(BLUE+"Pregunta N°4: ¿Como se llama la otra identidad de Peter Parker?")
  print(CYAN+"a)"+RESET+" Ironman")
  print(CYAN+"b)"+RESET+" Superman")
  print(CYAN+"c)"+RESET+" Spiderman")
  print(CYAN+"d)"+RESET+" Chespirito")
  
  respuesta_4 = input("\nTu respuesta: ")
  
  #Tiempo
  time.sleep(1)
  
  while respuesta_4 not in ("a", "b", "c", "d", "n"):
    respuesta_4 = input(RED+"\nNo es una de las alternativas, volver a intentarlo.\n\n"+RESET+"Ingresa nuevamente tu respuesta:")
    #Tiempo
    time.sleep(1)
  
  if respuesta_4 == "a":
    puntos = puntos + 5
    print(RED+"\nRespuesta incorrecta. Te sumamos 5 puntos\n")
  elif respuesta_4 == "b":
    puntos = puntos - 5
    print(RED+"\n Respuesta incorrecta. Te restamos 5 puntos :/ \n")
  elif respuesta_4 == "c":
    puntos = puntos * 2
    print(GREEN+"\nRespuesta correcta. Duplicas tus puntos.\n")
  elif respuesta_4 == "d":
    puntos = puntos / 2
    print(RED+"\nRespuesta incorrecta. Te quitamos la mitad de tus puntos\n")
  elif respuesta_4 == "n":
    puntos += 20
    print(MAGENTA+"\nEncontraste la alternativa secreta, ganastes 20 puntos.\n")
  
  #Tiempo
  time.sleep(1.5)
  
  #puntaje
  print(CYAN+"Tienes ", puntos, " puntos.\n")
  
  #Tiempo
  time.sleep(1)
  
  #juego de la ruleta
  print(YELLOW+"Ahora jugaremos a la ruleta, saldran 5 numeros en pantalla y el ultimo numero, te lo sumaremos a tus puntos, para que obtengas un puntaje mayor :) \n")
  
  #Tiempo
  time.sleep(6)
  
  for variable1 in range (0,5,+1):
    #Puntos aletorio
    puntajeAletorio = random.randint(0,30)
    print (RED,"N° ",variable1+1,": ",puntajeAletorio)
    time.sleep(1)
  
  puntajeFinal = puntos + puntajeAletorio
  
  #Tiempo
  time.sleep(2)
  
  #puntaje final
  print(CYAN+"\nTu puntaje final es de ",puntajeFinal, "puntos.")
  
  #Tiempo
  time.sleep(2)

  print("\n¿Deseas intentar la trivia nuevamente?")
  
  #Tiempo
  time.sleep(1)
  
  repetir_trivia = input("Ingresa 'si' para intentarlo de nuevo, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si": 
    #puntaje final
    print("\nHasta luego ",nombre," :) \n")
    iniciar_trivia = False

#Tiempo
time.sleep(1)
  
#Despedida
print(BLUE+"\nFin del programa :(\n")