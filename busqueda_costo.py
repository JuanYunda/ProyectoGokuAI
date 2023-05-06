import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import copy
from classNodoCosto import NodoCosto
import time

def busqueda_costo(mapa):

    profundidadFinal = 0
    colaDeNodos = deque()
    colaOrdenada = deque()

    inicio = time.time()
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 2:
                goku_row, goku_col = i, j

    nodoRaiz = NodoCosto(None, mapa, 0, goku_row, goku_col, "")
    nodo = nodoRaiz

    cantidadDeNodosExpandidos = 0

    while True:
        resultado = nodo
        cantidadDeNodosExpandidos += 1
        if nodo.getEsferas() == 2:
            profundidadFinal = nodo.getProfundidad()
            costoFinal = nodo.getCosto()
            resultado = nodo
            break

        else:
            if nodo.getGoku_col() < len(mapa[0]) - 1:
                if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col() + 1] != 1 and (
                    nodo.getMovimientoAnterior() != "left"
                    or nodo.getMovimientoAnterior() == ""
                ):  # right
                    copiaMapa1 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoCosto(
                        nodo,
                        copiaMapa1,
                        nodo.getProfundidad() + 1,
                        nodo.getGoku_row(),
                        nodo.getGoku_col(),
                        "right",
                    )
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_right()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_col() > 0:
                if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col() - 1] != 1 and (
                    nodo.getMovimientoAnterior() != "right"
                    or nodo.getMovimientoAnterior() == ""
                ):  # left
                    copiaMapa2 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoCosto(
                        nodo,
                        copiaMapa2,
                        nodo.getProfundidad() + 1,
                        nodo.getGoku_row(),
                        nodo.getGoku_col(),
                        "left",
                    )
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_left()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_row() < len(mapa) - 1:
                if nodo.getMapa()[nodo.getGoku_row() + 1][nodo.getGoku_col()] != 1 and (
                    nodo.getMovimientoAnterior() != "up"
                    or nodo.getMovimientoAnterior() == ""
                ):  # down
                    copiaMapa3 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoCosto(
                        nodo,
                        copiaMapa3,
                        nodo.getProfundidad() + 1,
                        nodo.getGoku_row(),
                        nodo.getGoku_col(),
                        "down",
                    )
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_down()
                    colaDeNodos.append(nuevoNodo)

            if nodo.getGoku_row() > 0:
                if nodo.getMapa()[nodo.getGoku_row() - 1][nodo.getGoku_col()] != 1 and (
                    nodo.getMovimientoAnterior() != "down"
                    or nodo.getMovimientoAnterior() == ""
                ):  # up
                    copiaMapa4 = copy.deepcopy(nodo.getMapa())
                    nuevoNodo = NodoCosto(
                        nodo,
                        copiaMapa4,
                        nodo.getProfundidad() + 1,
                        nodo.getGoku_row(),
                        nodo.getGoku_col(),
                        "up",
                    )
                    nuevoNodo.setEsferas(nodo.getEsferas())
                    nuevoNodo.setCosto(nodo.getCosto())
                    nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
                    nuevoNodo.setSemillas(nodo.getSemillas())
                    nuevoNodo.move_up()
                    colaDeNodos.append(nuevoNodo)

            colaOrdenada = sorted(colaDeNodos, key=NodoCosto.getCosto)
            colaDeNodos = deque(colaOrdenada)
            nodo = colaDeNodos.popleft()

    solucion = []

    # guarda los movimientos optimos para llegar a la solucion.
    # contiene desde el último movimiento solución hasta el primer movimiento (sin la raiz)
    while resultado.getPadre() != None:
        solucion.append(resultado.getMapa())
        resultado = resultado.getPadre()
        print(resultado.getCosto())
    print("solución registrada")
    fin = time.time()
    solucion.append(mapa)

    print("Cantidad de nodos expandidos:", cantidadDeNodosExpandidos)
    print("Profundidad de la solucion:", profundidadFinal)
    print("El tiempo tomado es de:", fin - inicio)
    print("Costo de la solución:", costoFinal)
    return solucion
