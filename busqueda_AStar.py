from collections import deque
import matplotlib.pyplot as plt
import copy
from classNodoInformada import NodoInformada
import subprocess
import time

#ProyectoGokuAI
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

def busqueda_A_Star(mapa):

    profundidadFinal = 0

    colaDeNodos = deque()
    colaOrdenada = deque() #cola que contiene los nodos sin expandir pero
                           # ordenados segun la suma de la heuristica y su costo (menor a mayor)

    goku_row, goku_col = 0, 0
    esf1_row, esf1_col, esf2_row, esf2_col = 0, 0, 0, 0
    esf1, esf2 = False, False
    flag = 0
    inicio = time.time()
    
    #ciclo for que busca a goku y cada esfera por toda la matriz/mapa
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 2:
                goku_row, goku_col = i, j
            if mapa[i][j] == 6 and flag == 0:#si en la posición i,j de la matriz se encuentra un numero 6
                                             #es porque esa es la posición de la primera esfera y se almacena
                esf1_row, esf1_col = i, j
                flag = 1 #flag que indica si ya se encontro la primera esfera
            elif mapa[i][j] == 6 and flag == 1:#si en la posición i,j de la matriz se encuentra un numero 6
                                               #es porque esa es la posición de la segunda esfera y se almacena
                esf2_row, esf2_col = i, j
                flag = 2 #flag que indica si ya se encontro la segunda esfera


    nodoRaiz = NodoInformada(None, mapa, 0, goku_row, goku_col, "", False, False)
    nodo = nodoRaiz
    cantidadDeNodosExpandidos = 0
    costoFinal = 0

    #ciclo while que expande nodos con menor costo+heuristica y crea sus nodo hijos
    while (True):
        cantidadDeNodosExpandidos += 1

        #condicional que verifica si ya se recogió la primera esfera (no necesariamente se recoge la primera antes que la segunda)
        if (nodo.getGoku_row() == esf1_row and nodo.getGoku_col() == esf1_col and not esf1):
            esf1 = nodo.setH1Obtenido()
        #condicional que verifica si ya se recogió la segunda esfera (no necesariamente se recoge la primera antes que la segunda)
        elif (nodo.getGoku_row() == esf2_row and nodo.getGoku_col() == esf2_col and not esf2):
            esf2 = nodo.setH2Obtenido()

        if nodo.getEsferas() == 2:
            profundidadFinal = nodo.getProfundidad()
            costoFinal = nodo.getCosto()
            resultado = nodo
            break

        else:
            if nodo.getGoku_col() < len(mapa[0])-1:
                if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()+1] != 1 and (nodo.getMovimientoAnterior() != "left" or nodo.getMovimientoAnterior() == ""):  # right
                    copiaMapa1 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoInformada(nodo, copiaMapa1, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "right", nodo.getH1Obtenido(), nodo.getH2Obtenido())
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_right()
                    nuevoNodo.setH1(esf1_col, esf1_row) #calcula la heurisitica a la primera esfera
                    nuevoNodo.setH2(esf2_col, esf2_row) #calcula la heurisitica de la segunda esfera
                    nuevoNodo.setH() #define cual de las dos esferas está mas cerca para asignar esta como principal objetivo
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_col() > 0:
                if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()-1] != 1 and (nodo.getMovimientoAnterior() != "right" or nodo.getMovimientoAnterior() == ""):  # left
                    copiaMapa2 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoInformada(nodo, copiaMapa2, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "left", nodo.getH1Obtenido(), nodo.getH2Obtenido())
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_left()
                    nuevoNodo.setH1(esf1_col, esf1_row)
                    nuevoNodo.setH2(esf2_col, esf2_row)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_row() < len(mapa)-1:
                if nodo.getMapa()[nodo.getGoku_row()+1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "up" or nodo.getMovimientoAnterior() == ""):  # down
                    copiaMapa3 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoInformada(nodo, copiaMapa3, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "down", nodo.getH1Obtenido(), nodo.getH2Obtenido())
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_down()
                    nuevoNodo.setH1(esf1_col, esf1_row)
                    nuevoNodo.setH2(esf2_col, esf2_row)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_row() > 0:
                if nodo.getMapa()[nodo.getGoku_row()-1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "down" or nodo.getMovimientoAnterior() == ""):  # up
                    copiaMapa4 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoInformada(nodo, copiaMapa4, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "up", nodo.getH1Obtenido(), nodo.getH2Obtenido())
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_up()
                    nuevoNodo.setH1(esf1_col, esf1_row)
                    nuevoNodo.setH2(esf2_col, esf2_row)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)

            colaOrdenada = sorted(colaDeNodos, key=NodoInformada.getHAStar) #ordena la cola de nodos segun la heurisitca+costo (funcion getHAStar devuelve la suma) (ordena de menor a mayor)
            colaDeNodos = deque(colaOrdenada) #redefine la cola de nodos ya ordenada
            nodo = colaDeNodos.popleft()
    solucion = []

    # guarda los movimientos optimos para llegar a la solucion.
    # contiene desde el último movimiento solución hasta el primer movimiento (sin la raiz)
    while resultado.getPadre() != None:
        solucion.append(resultado.getMapa())
        resultado = resultado.getPadre()
    fin = time.time()

    solucion.append(mapa)

    return solucion, cantidadDeNodosExpandidos, profundidadFinal, fin - inicio, costoFinal
