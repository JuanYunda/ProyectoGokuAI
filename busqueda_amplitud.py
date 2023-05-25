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
    
    colaDeNodos = deque() #cola de nodos creados (el primero de la cola es el que se va a expandir)
    inicio = time.time() #empieza a contar el tiempo que demora el algoritmo
    cantidadDeNodosExpandidos = 0 #variable que cuenta cuantos nodos fueron expandidos

    #ciclo for que busca a goku por toda la matriz/mapa
    for i in range(len(mapa)): #for de las filas
      for j in range(len(mapa[i])): #for de las columnas
        if mapa[i][j] == 2:
          goku_row, goku_col = i, j #si en la posición i,j de la matriz se encuentra un numero 2
                                    #es porque esa es la posición del goku y se almacena

    nodoRaiz = Nodo(None, mapa, 0, goku_row, goku_col, "") #nodo inicial raiz del arbol que guarda el
                                                           #ambiente inicial de la busqueda

    nodo = nodoRaiz #se almacena el nodo raiz en una variable (con el fin de dar coherencia al while)

    #ciclo while que expande nodos y crea sus nodo hijos
    while(True):
      cantidadDeNodosExpandidos += 1 #el codigo empieza con la expanción de un nuevo nodo, por lo que se
                                     #aumenta la cantidad de nodos expandidos

      #condicional que verifica si el nodo a expandir encontró la solución
      if nodo.getEsferas()==2:
                               #en su ambiente (goku tiene 2 esferas)
        profundidadFinal = nodo.getProfundidad() #obtiene la profundidad del nodo solución y almacena
                                                 #dicho numero en la variable 
        resultado = nodo #almacena el nodo solución en una variable resultado
        break

      #condicional que crea los nodos hijo del nodo que se esta expandiendo
      else:

        #condicional que verifica si goku se puede mover a la derecha sin salirse del mapa
        if nodo.getGoku_col() < len(mapa[0])-1:
          #condicional que verifica si goku no tiene una pared (numero 1 en la matriz) a la derecha y
          # si no viene de la derecha (no devolverse)
          if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()+1] != 1 and (nodo.getMovimientoAnterior() != "left" or nodo.getMovimientoAnterior() == ""): #right
            copiaMapa1 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa1, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "right")
            #se crea un nodo que es una copia del anterior, con profundidad+1, que identifica que se va a mover a la derecha y tiene de padre a su nodo padre
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_right() #se mueve a la derecha. esto implica agarrar objetos o
                                   #enfrentarse a enemigos
            colaDeNodos.append(nuevoNodo) #se agrega al final de la cola de nodos

        #condicional que verifica si goku se puede mover a la izquierda sin salirse del mapa
        if nodo.getGoku_col() > 0:
          #condicional que verifica si goku no tiene una pared (numero 1 en la matriz) a la izquierda y
          # si no viene de la izquierda (no devolverse)
          if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()-1] != 1 and (nodo.getMovimientoAnterior() != "right" or nodo.getMovimientoAnterior() == ""): #left
            copiaMapa2 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa2, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "left")
            #se crea un nodo que es una copia del anterior, con profundidad+1, que identifica que se va a mover a la izquierda y tiene de padre a su nodo padre
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_left() #se mueve a la izqueirda. esto implica agarrar objetos o
                                  #enfrentarse a enemigos
            colaDeNodos.append(nuevoNodo) #se agrega al final de la cola de nodos

        #condicional que verifica si goku se puede mover abajo sin salirse del mapa
        if nodo.getGoku_row() < len(mapa)-1:
          #condicional que verifica si goku no tiene una pared (numero 1 en la matriz) abajo y
          # si no viene de abajo (no devolverse)
          if nodo.getMapa()[nodo.getGoku_row()+1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "up" or nodo.getMovimientoAnterior() == ""): #down
            copiaMapa3 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa3, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "down")
            #se crea un nodo que es una copia del anterior, con profundidad+1, que identifica que se va a mover abajo y tiene de padre a su nodo padre
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_down() #se mueve abajo. esto implica agarrar objetos o
                                  #enfrentarse a enemigos
            colaDeNodos.append(nuevoNodo) #se agrega al final de la cola de nodos

        #condicional que verifica si goku se puede mover arriba sin salirse del mapa
        if nodo.getGoku_row() > 0:
          #condicional que verifica si goku no tiene una pared (numero 1 en la matriz) arriba y
          # si no viene de arriba (no devolverse)
          if nodo.getMapa()[nodo.getGoku_row()-1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "down" or nodo.getMovimientoAnterior() == ""): #up
            copiaMapa4 = copy.deepcopy(nodo.getMapa())
            nuevoNodo = Nodo(nodo, copiaMapa4, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "up")
            #se crea un nodo que es una copia del anterior, con profundidad+1, que identifica que se va a mover arriba y tiene de padre a su nodo padre
            nuevoNodo.setEsferas(nodo.getEsferas())
            nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
            nuevoNodo.setSemillas(nodo.getSemillas())
            nuevoNodo.move_up() #se mueve arriba. esto implica agarrar objetos o
                                #enfrentarse a enemigos
            colaDeNodos.append(nuevoNodo) #se agrega al final de la cola de nodos

        nodo = colaDeNodos.popleft() #se elimina el primer nodo de la cola y se almacena en la variable

    solucion = [] #array que almacena la matriz/mapa de cada paso para lleagr a la solcuión
                  #(pasos al revez, del nodo resultado al hijo del nodo raiz)

    # guarda los movimientos optimos para llegar a la solucion.
    # contiene desde el último movimiento solución hasta el primer movimiento (sin la raiz)
    while resultado.getPadre() != None:
      solucion.append(resultado.getMapa()) #obtiene el mapa de cada paso y lo almacena en el array solución
      resultado = resultado.getPadre() #continua con el anterior paso para llegar a la solución (padre)
    print("solución registrada")
    fin = time.time() #detiene el conteo de tiempo

    solucion.append(mapa) #concatena la matriz/mapa inicial

    """for i in reversed(solucion):
      plt.imshow(i.getMapa(), cmap='hot', interpolation='nearest')
      plt.show()""" 

    return solucion, cantidadDeNodosExpandidos, profundidadFinal, fin - inicio

    #subprocess.Popen(["python", "GUI.py"])

