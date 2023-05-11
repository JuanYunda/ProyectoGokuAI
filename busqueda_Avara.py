from collections import deque
import matplotlib.pyplot as plt
import copy
from classNodoAvara import NodoAvara
import subprocess
import time

def busqueda_Avara(mapa):
    profundidadFinal = 0
    colaDeNodos = deque()
    colaHeuristica = deque()
    goku_row, goku_col = 0, 0
    esf1_row, esf1_col, esf2_row, esf2_col = 0, 0, 0, 0
    flagCiclo = False
    left, right, up, down = True, True, True, True
    flag = 0
    inicio = time.time()
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 2:
                goku_row, goku_col = i, j
            if mapa[i][j] == 6 and flag == 0:
                esf1_row, esf1_col = i, j
                flag = 1
            if mapa[i][j] == 6 and flag == 1:
                esf2_row, esf2_col = i, j


    nodoRaiz = NodoAvara(None, mapa, 0, goku_row, goku_col, "")
    nodo = nodoRaiz
    cantidadDeNodosExpandidos = 0
    costoFinal = 0
    # a=0
    while (True):
        resultado = nodo
        cantidadDeNodosExpandidos += 1
        if nodo.getEsferas() == 2:
            profundidadFinal = nodo.getProfundidad()
            costoFinal = nodo.getCosto()
            resultado = nodo
            break

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
                if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()+1] != 1 and (nodo.getMovimientoAnterior() != "left" or nodo.getMovimientoAnterior() == ""):  # right
                    copiaMapa1 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoAvara(nodo, copiaMapa1, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "right")
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_right()
                    nuevoNodo.setH1(esf1_row, esf1_col)
                    nuevoNodo.setH2(esf2_row, esf2_col)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_col() > 0 and left:
                if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()-1] != 1 and (nodo.getMovimientoAnterior() != "right" or nodo.getMovimientoAnterior() == ""):  # left
                    copiaMapa2 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoAvara(nodo, copiaMapa2, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "left")
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_left()
                    nuevoNodo.setH1(esf1_row, esf1_col)
                    nuevoNodo.setH2(esf2_row, esf2_col)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)
            
            if nodo.getGoku_row() < len(mapa)-1 and down:
                if nodo.getMapa()[nodo.getGoku_row()+1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "up" or nodo.getMovimientoAnterior() == ""):  # down
                    copiaMapa3 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoAvara(nodo, copiaMapa3, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "down")
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_down()
                    nuevoNodo.setH1(esf1_row, esf1_col)
                    nuevoNodo.setH2(esf2_row, esf2_col)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_row() > 0 and up:
                if nodo.getMapa()[nodo.getGoku_row()-1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "down" or nodo.getMovimientoAnterior() == ""):  # up
                    copiaMapa4 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoAvara(nodo, copiaMapa4, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "up")
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_up()
                    nuevoNodo.setH1(esf1_row, esf1_col)
                    nuevoNodo.setH2(esf2_row, esf2_col)
                    nuevoNodo.setH()
                    colaDeNodos.append(nuevoNodo)
        

            if (nodo.getGoku_row == esf1_row and nodo.getGoku_col == esf1_col):
                esf1_row, esf1_col = 0, 0
            if (nodo.getGoku_row == esf2_row and nodo.getGoku_col == esf2_col):
                esf2_row, esf2_col = 0, 0

            colaHeuristica = sorted(colaDeNodos, key=NodoAvara.getH)
            colaDeNodos = deque(colaHeuristica)
            nodo = colaDeNodos.popleft()
            left, right, up, down = True, True, True, True
            flagCiclo = False

    solucion = []

    # guarda los movimientos optimos para llegar a la solucion.
    # contiene desde el último movimiento solución hasta el primer movimiento (sin la raiz)
    while resultado.getPadre() != None:
        solucion.append(resultado.getMapa())
        resultado = resultado.getPadre()
    fin = time.time()
    print("solución registrada")

    solucion.append(mapa)

    return solucion, cantidadDeNodosExpandidos, profundidadFinal, fin - inicio, costoFinal
