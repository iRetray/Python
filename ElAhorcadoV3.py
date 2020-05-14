import random
'''
AYPR PARCIAL DE TERCER CORTE
APELLIDOS Y NOMBRES: Joan Sebastian Obando Estupiñann
FECHA: 12/05/2020
'''
def dibujar(vida):
  matrizVida5 = [
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' * ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * ']
  ]
  matrizVida4 = [
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' * ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * ']
  ]
  matrizVida3 = [
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' * ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * ']
  ]
  matrizVida2 = [
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' * ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' * ']
  ]
  matrizVida1 = [
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' * ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' * ',' - ',' - ',' - ',' - ',' - ',' - ',' * ']
  ]
  matrizVida0 = [
      [' - ',' - ',' - ',' * ',' * ',' * ',' * ',' * ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' * ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' * ',' * ',' * ',' * ',' * ',' * ',' * ',' - ',' * '],
      [' - ',' - ',' - ',' * ',' - ',' - ',' - ',' - ',' * '],
      [' - ',' - ',' * ',' - ',' * ',' - ',' - ',' - ',' * '],
      [' - ',' * ',' - ',' - ',' - ',' * ',' - ',' - ',' * ']
  ]
  if vida == 5:
    for x in range(0,10):
      linea = ""
      for y in range(0,9):
        linea = linea + str(matrizVida5[x][y])
      print(linea)
  if vida == 4:
    for x in range(0,10):
      linea = ""
      for y in range(0,9):
        linea = linea + str(matrizVida4[x][y])
      print(linea)
  if vida == 3:
    for x in range(0,10):
      linea = ""
      for y in range(0,9):
        linea = linea + str(matrizVida3[x][y])
      print(linea)
  if vida == 2:
    for x in range(0,10):
      linea = ""
      for y in range(0,9):
        linea = linea + str(matrizVida2[x][y])
      print(linea)
  if vida == 1:
    for x in range(0,10):
      linea = ""
      for y in range(0,9):
        linea = linea + str(matrizVida1[x][y])
      print(linea)
  if vida == 0:
    for x in range(0,10):
      linea = ""
      for y in range(0,9):
        linea = linea + str(matrizVida0[x][y])
      print(linea)


def palabras():
    matriz_palabras = [
        ['pera','mango','piña','uva','naranja','papaya','melon','manzana','kiwi','patilla'],
        ['colombia','argentina','españa','francia','inglaterra','japon','alemania','rusia','china','peru'],
        ['alejandro','maria','evelyn','daniel','brayan','roberto','juliana','valentina','andres','esperanza'],
        ['ingeniero','profesor','abogado','arquitecto','locutor','pintor','medico','vendedor','diseñador','cantante'],
        ['tigre','perro','gato','jirafa','hipopotamo','jabali','pantera','loro','ornitorrinco','rinoceronte'],
    ]
    fila = random.randrange(5);
    columna = random.randrange(10);
    objeto = matriz_palabras[fila][columna];
    if fila==0:
      pista = "Fruta";
    if fila==1:
      pista = "Pais";
    if fila==2:
      pista = "Nombre";
    if fila==3:
      pista = "Profesion";
    if fila==4:
      pista = "Animal";
    return objeto, pista

def main():
    # Mensaje de bienvenida
    print('\nBienvenido al juego del ahorcado.\n')
    # Escoger palabra aleatoria
    objeto, pista = palabras()
    print('\nLa palabra es:',objeto)
    print('PISTAS:')
    print('-La palabra es un(a):',pista)
    print('-La palabra tiene',len(objeto),'letras')
    lista = list(objeto)
    listaVacia = list(objeto)
    palabrasElegidas = [" "]
    for x in range(0,len(listaVacia)):
      listaVacia[x] = '_'
    juegoNoResuelto = True;
    vidas = 5
    while juegoNoResuelto:
      dibujar(vidas)
      print("\nIngresa un caracter:")
      letra = input()
      letraRepetida = False      
      for x in palabrasElegidas:
        if x==letra:
          vidas = vidas-1
          print("Ya habias elegido esa letra (Quedan",vidas,"vidas)")
          letraRepetida = True          
      palabrasElegidas.append(letra)
      letraCorrecta = False 
      if letraRepetida == False:    
        for x in range(0,len(lista)):
          if lista[x] == letra:
            letraCorrecta = True
            listaVacia[x] = lista[x]        
        if letraCorrecta:
          print("\nLetra acertada")
        else:
          vidas = vidas-1
          print("\nLetra fallida (Quedan",vidas,"vidas)")   
        progreso = ""
        for x in range(0,len(listaVacia)):
          progreso = progreso + str(listaVacia[x]) + " "   
        print(progreso)
        if lista == listaVacia:
          print("\nHas adivinado la palabra")
          juegoNoResuelto = False
      if vidas==0:
        print("\nHas perdido todas tus vidas")
        juegoNoResuelto = False

jugarOtraVez = True
while jugarOtraVez:
  main()
  print("¿Quiere jugar otra vez? (S/N)")
  opcion = input()
  if opcion=="S" or opcion=="s":
    jugarOtraVez = True
  else:
    jugarOtraVez = False
print('\nGracias por jugar al ahorcado.\n')