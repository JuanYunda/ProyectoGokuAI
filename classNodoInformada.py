import numpy as np

#ProyectoGokuAI
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

class NodoInformada:
  # ESTADO:
  #  self.padre = el padre de un nodo
  #  self.mapa = estado del mapa actualmente
  #  self.profundidad = nivel del arbol donde se encuentra el nodo
  #  self.goku_row, self.goku_col = posicion de goku *antes de moverse*
  #  self.movimientoAnterior = cual fue el anterior movimiento de goku
  #  self.h1Obtenido, h2Obtenido = indica si la esfera 1 o 2 fue obtenida
    
  def __init__(self, padre, mapaActual, profundidad, goku_row, goku_col, movimientoAnterior, h1Obtenido, h2Obtenido):
    self.mapa = mapaActual
    self.padre = padre
    self.profundidad = profundidad
    self.goku_row = goku_row
    self.goku_col = goku_col
    self.esferas = 0 #variable que guarda cuantas esferas tiene goku
    self.semillas = 0 #variable que guarda cuantas semillas tiene goku
    self.costo = 0 #variable que guarda el costo del nodo
    self.movimientoAnterior = movimientoAnterior
    self.ultimaCasilla = 0 #variable que guarda que había en la anterior casilla 
    self.heuristica, self.h1, self.h2 = 0,0,0 #variables que guardan la heurisitica que se va a utilizar, la heuristica a la esfera 1 y esfera 2
    self.H1Obtenida = h1Obtenido
    self.H2Obtenida = h2Obtenido
    
  #funciones de movimiento de Goku

  def move_right(self):
      #asigna el valor correspondiente a la casilla donde esta el goku antes estar alli
      #un 0 si era un 0, una esfera, una semilla o derrotó a un enemigo
      #sino deja el valor del enemigo que no pudo derrotar
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row][self.goku_col+1]==6):
        self.setEsferas(self.esferas+1) #aumenta las esferas
        self.movimientoAnterior="" #reinicia la variable que permite devolverse

      self.funcion_costo(0, 1) #ejecuta una funcion que está mas adelante (muy importante)

      self.mapa[self.goku_row][self.goku_col+1] = 2 #mueve goku a la derecha
      self.goku_col = self.goku_col+1 #sincroniza las coordenadas de goku
      #print("se mueve derecha")

  def move_left(self):
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row][self.goku_col-1]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""

      self.funcion_costo(0, -1)

      self.mapa[self.goku_row][self.goku_col-1] = 2 #mueve goku a la izquierda
      self.goku_col = self.goku_col-1 #sincroniza las coordenadas de goku
      #print("se mueve izquierda")

  def move_up(self):
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row-1][self.goku_col]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""

      self.funcion_costo(-1, 0)

      self.mapa[self.goku_row-1][self.goku_col] = 2 #mueve goku arriba
      self.goku_row = self.goku_row-1 #sincroniza las coordenadas de goku
      #print("se mueve arriba")

  def move_down(self):
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row+1][self.goku_col]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""

      self.funcion_costo(1, 0)

      self.mapa[self.goku_row+1][self.goku_col] = 2 #mueve goku arriba
      self.goku_row = self.goku_row+1 #sincroniza las coordenadas de goku
      #print("se mueve abajo")

#Costos: 
#Casilla vacia y con semilla: 1
#Casilla con freezer sin semilla: 3 + 1
#Casilla con freezer con semilla (desaparece): 1
#Casilla con Cell sin semilla: 6 + 1
#Casilla con Cell con semilla (desaparece): 1

  #funcion que se encarga de verificar que acciones se hacen teniendo en cuenta que hay en la casilla donde se va a mover el goku
  def funcion_costo(self, fila, columna):
    costo=0
    
    #verifica si la siguiente casilla tiene una semilla
    if (self.mapa[(self.goku_row)+fila][(self.goku_col)+columna] == 5):
        self.aumentarSemillas(1) #aumenta las semillas
        self.movimientoAnterior="" #permite devolverse (olvida su ultimo movimiento)

    #si hay un freezer
    elif (self.mapa[(self.goku_row)+fila][(self.goku_col)+columna] == 3):
      #si no tiene semillas
      if self.semillas == 0:
        costo = 3 #asigna el costo añadido correspondiente (por pasar por el enemigo)
        self.setUltimaCasilla(3) #no derrota al enemigo
      #si tiene semillas
      else:
        costo = 0 #sin costo añadido (derrota al enemigo, usa la semilla y no cuesta nada)
        self.aumentarSemillas(-1) #gasta unas semilla
        self.setUltimaCasilla(0) #derrota al enemigo
      self.movimientoAnterior="" #permite devolverse (olvida su ultimo movimiento)

    #si hay un cell y no hay semillas
    elif (self.mapa[(self.goku_row)+fila][(self.goku_col)+columna] == 4):
      if self.semillas == 0:
        costo = 6
        self.setUltimaCasilla(4)
      else:
        costo = 0
        self.aumentarSemillas(-1)
        self.setUltimaCasilla(0)
      self.movimientoAnterior="" #permite devolverse (olvida su ultimo movimiento)
        
    #la siguiente casilla no tiene nada
    else:
      self.setUltimaCasilla(0) #entonces se dejará nada en esa casilla

    self.aumentarCosto(costo+1) #suma el costo añadido mas el costo fijo de moverse
    
  #funcion que aumenta el costo una cantidad fija mas el costo de su nodo padre
  def aumentarCosto(self, cantidad):
    self.costo += cantidad

  #funcion que aumenta o disminuye las semillas una cantidad fija (+1 o -1)
  def aumentarSemillas(self, cantidad):
    self.semillas += cantidad

  #metodos get

  def getPadre(self):
    return self.padre

  def getMapa(self):
    return self.mapa

  def getEsferas(self):
    return self.esferas

  def getGoku_row(self):
    return self.goku_row
    
  def getGoku_col(self):
    return self.goku_col

  def getProfundidad(self):
    return self.profundidad

  def getMovimientoAnterior(self):
    return self.movimientoAnterior

  def getUltimaCasilla(self):
    return self.ultimaCasilla

  def getCosto(self):
    return self.costo

  def getSemillas(self):
    return self.semillas
  
  def getH1(self):
    return self.h1
  
  def getH2(self):
    return self.h2

  #retorna el costo total del nodo (heuristica+costo)
  def getHAStar(self):
    return self.heuristica+self.costo
  
  def getH1Obtenido(self):
    return self.H1Obtenida
  
  def getH2Obtenido(self):
    return self.H2Obtenida
  
  def getHAvara(self):
    return self.heuristica
  
  #metodos set

  #asigna la cantidad de esferas una cantidad fija
  def setEsferas(self, cantidad):
    self.esferas = cantidad

  #asigna cual es la ultima casilla que remplazar cuando goku se mueva
  def setUltimaCasilla(self, cantidad):
    self.ultimaCasilla = cantidad

  #asigna el costo en una cantidad fija (costo del padre y luego se suma con el costo de moverse)
  def setCosto(self, cantidad):
    self.costo = cantidad

  #asigna una cantidad de semillas fija (semillas del padre y luego se cambia si obtiene alguna o gasta una)
  def setSemillas(self, cantidad):
    self.semillas = cantidad

  #calcula la heuristica a la esfera #1 con distancia de euler
  def setH1(self,x,y):
    #verifica si ya se ha obtenido la esfera #1
    if self.H1Obtenida:
      self.h1 = 0
    else: 
      self.h1 = np.sqrt((x-self.goku_col) ** 2 + (y-self.goku_row) ** 2)

  #calcula la heuristica a la esfera #2 con distancia de euler
  def setH2(self,x,y):
    #verifica si ya se ha obtenido la esfera #2
    if self.H2Obtenida:
      self.h2 = 0
    else: 
      self.h2 = np.sqrt((x-self.goku_col) ** 2 + (y-self.goku_row) ** 2)

  #asigna si ya se obtuvo la esfera #1
  def setH1Obtenido(self):
    self.H1Obtenida = True
    return True
  
  #asigna si ya se obtuvo la esfera #2
  def setH2Obtenido(self):
    self.H2Obtenida = True
    return True

  #define que valor de heuristica se le va a asignar al nodo
  def setH(self):
    #si ya se obtuvo la esfera #1, se deja la heuristica de la esfera #2
    if(self.H1Obtenida):
      self.heuristica = self.h2
      return None
    #si ya se obtuvo la esfera #2, se deja la heuristica de la esfera #1
    elif(self.H2Obtenida):
      self.heuristica = self.h1
      return None

    #verifica que esfera tiene una heuristica menor para marcarla como objetivo, es decir, asignar su heurisitica al nodo 
    if(self.h1 >= self.h2):
      self.heuristica = self.h2 
    else:
      self.heuristica = self.h1