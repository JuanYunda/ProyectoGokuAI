class Nodo:
  # ESTADO:
  #  self.padre = el padre de un nodo
  #  self.mapa = estado del mapa actualmente
  #  self.profundidad = nivel del arbol donde se encuentra el nodo
  #  self.goku_row, self.goku_col = posicion de goku *antes de moverse*
  #  self.esferas = cuantas esferas tiene goku
  #  self.anterior_row, self.anterior_col = posicion previa de Goku
    
  def __init__(self, padre, mapaActual, profundidad, goku_row, goku_col, movimientoAnterior):
    self.mapa = mapaActual
    self.padre = padre
    self.profundidad = profundidad
    self.goku_row = goku_row
    self.goku_col = goku_col
    self.esferas = 0
    self.movimientoAnterior = movimientoAnterior
    self.ultimaCasilla = 0
  #funciones de movimiento de Goku

  def move_right(self):
      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row][self.goku_col+1]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""
      self.mapa[self.goku_row][self.goku_col] = 0
      self.mapa[self.goku_row][self.goku_col+1] = 2
      self.goku_col = self.goku_col+1
      #print("se mueve derecha")

  def move_right(self):
      #Revisar si en la posicion a la que se va a mover hay una esfera
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      if(self.mapa[self.goku_row][self.goku_col+1]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""

      self.recordar_enemigos(0, 1)

      self.mapa[self.goku_row][self.goku_col+1] = 2
      self.goku_col = self.goku_col+1
      #print("se mueve derecha")

  def move_left(self):
      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row][self.goku_col-1]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      self.recordar_enemigos(0, -1)

      self.mapa[self.goku_row][self.goku_col-1] = 2
      self.goku_col = self.goku_col-1
      #print("se mueve izquierda")

  def move_up(self):
      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row-1][self.goku_col]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      self.recordar_enemigos(-1, 0)

      self.mapa[self.goku_row-1][self.goku_col] = 2
      self.goku_row = self.goku_row-1
      #print("se mueve arriba")

  def move_down(self):
      #Revisar si en la posicion a la que se va a mover hay una esfera
      if(self.mapa[self.goku_row+1][self.goku_col]==6):
        self.setEsferas(self.esferas+1)
        self.movimientoAnterior=""
      self.mapa[self.goku_row][self.goku_col] = self.ultimaCasilla

      self.recordar_enemigos(1, 0)

      self.mapa[self.goku_row+1][self.goku_col] = 2
      self.goku_row = self.goku_row+1
      #print("se mueve abajo")

  def recordar_enemigos(self, fila, columna):

    #si hay un freezer
    if (self.mapa[(self.goku_row)+fila][(self.goku_col)+columna] == 3):
      self.setUltimaCasilla(3)
    else:
      self.setUltimaCasilla(0)

    #si hay un cell
    if (self.mapa[(self.goku_row)+fila][(self.goku_col)+columna] == 4):
      self.setUltimaCasilla(4)
    else:
      self.setUltimaCasilla(0)

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

  #metodos set

  def setEsferas(self, cantidad):
    #print("Se ha obtenido una esfera del dragón")
    self.esferas = cantidad

  def setUltimaCasilla(self, cantidad):
    self.ultimaCasilla = cantidad

  

