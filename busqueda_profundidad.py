from collections import deque
import matplotlib.pyplot as plt
import copy
from classNodo import Nodo
import numpy as np 
import subprocess
import time

#La busqueda por profundidad se caracteriza por agregar los nuevos nodos a la izquierda del arreglo en lugar de la derecha. 
#Tomará estos nodos primero y los recorrerá
def busqueda_profundidad(mapa):
    
    #Se asigna como valores globales la profundidad final, la cola de nodos, y la posicion xy de goku. También se tiene un contador de los nodos
    #Que se obtienen en el proceso
    profundidadFinal = 0
    colaDeNodos = deque()
    goku_row, goku_col = 0, 0
    nodosObtenidos = 0  
    inicio = time.time()
    flagCiclo = False
    left, right, up, down = True, True, True, True
    #Me recorre todo el mapa para encontrar la posición inicial
    for i in range(len(mapa)):
      for j in range(len(mapa[i])):
        if mapa[i][j] == 2:
          goku_row, goku_col = i, j
    
    #Se crea el nodo raiz para comenzar la busqueda
    nodoRaiz = Nodo(None, mapa, 0, goku_row, goku_col, "")
    nodo = nodoRaiz

    #Se trabaja un ciclo while para el proceso
    while(True):
      #resultado me refiere a la idea de que el nodo actual sea el final. Por defecto siempre apunta al nodo actual
      resultado = nodo
      nodosObtenidos+=1
      #Cuando se tenga las esferas, se termina el ciclo while, se me pasa la profundidad final y el nodo actual

      if nodo.getEsferas()==2:
        profundidadFinal = nodo.getProfundidad()
        resultado = nodo
        break

      #De lo contrario, se me recorre el mapa. La prioridad es: Derecha, Izquierda, Abajo, Arriba
      #El método de profundidad me recorre las posibilidades, y luego me expande la última posibilidad encontrada. Es decir
      #Si realiza un movimiendo de izquierda y leugo uno de derecha para el nodo padre, profundidad me seguirá con expandir el de la derecha primero
      else:
        navegar = nodo
        for i in range(len(mapa)):
          if flagCiclo:
            break
          for j in range(len(mapa[i])):
            if navegar.getPadre() != None:
              if navegar.getPadre().getEsferas() != nodo.getEsferas():
                flagCiclo = True
                break
              if nodo.getGoku_row() == navegar.getPadre().getGoku_row() and nodo.getGoku_col()-1 == navegar.getPadre().getGoku_col():
                left = False
              if nodo.getGoku_row() == navegar.getPadre().getGoku_row() and nodo.getGoku_col()+1 == navegar.getPadre().getGoku_col():
                right = False
              if nodo.getGoku_row()-1 == navegar.getPadre().getGoku_row() and nodo.getGoku_col() == navegar.getPadre().getGoku_col():
                up = False
              if nodo.getGoku_row()+1 == navegar.getPadre().getGoku_row() and nodo.getGoku_col() == navegar.getPadre().getGoku_col():
                down = False
              navegar = navegar.getPadre()

        if nodo.getGoku_col() < len(mapa[0])-1 and right:
          if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()+1] != 1 and (nodo.getMovimientoAnterior() != "left" or nodo.getMovimientoAnterior() == ""): #right
            copiaMapa = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "right")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.move_right()
            colaDeNodos.appendleft(nuevoNodo)

        if nodo.getGoku_col() > 0 and left:
          if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()-1] != 1 and (nodo.getMovimientoAnterior() != "right" or nodo.getMovimientoAnterior() == ""): #left
            copiaMapa = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "left")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.move_left()
            colaDeNodos.appendleft(nuevoNodo)

        if nodo.getGoku_row() < len(mapa)-1 and down:
          if nodo.getMapa()[nodo.getGoku_row()+1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "up" or nodo.getMovimientoAnterior() == ""): #down
            copiaMapa = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "down")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.move_down()
            colaDeNodos.appendleft(nuevoNodo)

        if nodo.getGoku_row() > 0 and up:
          if nodo.getMapa()[nodo.getGoku_row()-1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "down" or nodo.getMovimientoAnterior() == ""): #up
            copiaMapa = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "up")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.move_up()
            colaDeNodos.appendleft(nuevoNodo)

        nodo = colaDeNodos.popleft()
        left, right, up, down = True, True, True, True
        flagCiclo = False
    #Luego de finalizar el ciclo, se crea un arreglo de solución
    #Como cada nodo sabe cual es su padre, entonces me recorre los nodos de padre a padre
    #Hasta llegar al nodo inicial.
    #Luego se me agrega el mapa a la solución y se me retorna.
    solucion = []
    while resultado.getPadre() != None:
      solucion.append(resultado.getMapa())
      resultado = resultado.getPadre()

    solucion.append(mapa)
    fin = time.time()
    return solucion, nodosObtenidos, profundidadFinal, fin-inicio