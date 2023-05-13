import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import copy
from classNodo import Nodo
import subprocess
import time

#ProyectoGokuAI
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

def busqueda_amplitud(mapa):
    
    profundidadFinal = 0
    colaDeNodos = deque()
    inicio = time.time()
    goku_row, goku_col = 0, 0 
    cantidadDeNodosExpandidos = 0  

    for i in range(len(mapa)):
      for j in range(len(mapa[i])):
        if mapa[i][j] == 2:
          goku_row, goku_col = i, j

    nodoRaiz = Nodo(None, mapa, 0, goku_row, goku_col, "")
    nodo = nodoRaiz

    #a=0
    while(True):
      resultado = nodo
      cantidadDeNodosExpandidos += 1

      if nodo.getEsferas()==2:
        profundidadFinal = nodo.getProfundidad()
        resultado = nodo
        break

      else:

        if nodo.getGoku_col() < len(mapa[0])-1:
          if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()+1] != 1 and (nodo.getMovimientoAnterior() != "left" or nodo.getMovimientoAnterior() == ""): #right
            copiaMapa1 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa1, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "right")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_right()
            colaDeNodos.append(nuevoNodo)

        if nodo.getGoku_col() > 0:
          if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()-1] != 1 and (nodo.getMovimientoAnterior() != "right" or nodo.getMovimientoAnterior() == ""): #left
            copiaMapa2 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa2, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "left")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_left()
            colaDeNodos.append(nuevoNodo)

        if nodo.getGoku_row() < len(mapa)-1:
          if nodo.getMapa()[nodo.getGoku_row()+1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "up" or nodo.getMovimientoAnterior() == ""): #down
            copiaMapa3 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa3, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "down")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_down()
            colaDeNodos.append(nuevoNodo)

        if nodo.getGoku_row() > 0:
          if nodo.getMapa()[nodo.getGoku_row()-1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "down" or nodo.getMovimientoAnterior() == ""): #up
            copiaMapa4 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa4, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "up")
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_up()
            colaDeNodos.append(nuevoNodo)

        nodo = colaDeNodos.popleft()

    solucion = []

    # guarda los movimientos optimos para llegar a la solucion.
    # contiene desde el último movimiento solución hasta el primer movimiento (sin la raiz)
    while resultado.getPadre() != None:
      solucion.append(resultado.getMapa())
      resultado = resultado.getPadre()
    print("solución registrada")
    fin = time.time()

    solucion.append(mapa)

    """for i in reversed(solucion):
      plt.imshow(i.getMapa(), cmap='hot', interpolation='nearest')
      plt.show()""" 

    return solucion, cantidadDeNodosExpandidos, profundidadFinal, fin - inicio

    #subprocess.Popen(["python", "GUI.py"])

