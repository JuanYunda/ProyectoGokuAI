from collections import deque
import copy
import time
from classNodoCosto import NodoCosto

#ProyectoGokuAI
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

def busqueda_costo(mapa):
  profundidadFinal = 0
  colaDeNodos = deque()
  colaOrdenada = deque()

  inicio = time.time()
  for i in range(len(mapa)):
   for j in range(len(mapa[i])):
     if mapa[i][j] == 2:
       goku_row, goku_col = i, j

  nodoRaiz = NodoCosto(None, mapa, 0, goku_row, goku_col, "empty")
  nodo = nodoRaiz
  cantidadDeNodosExpandidos = 0
  flag = False
  costoFinal = 0
  left, right, up, down = True, True, True, True
  while(True):
   resultado = nodo
   cantidadDeNodosExpandidos += 1
   if nodo.getEsferas()==2:
     profundidadFinal = nodo.getProfundidad()
     costoFinal = nodo.getCosto()
     resultado = nodo
     break

   else:

     navegar = nodo
     for i in range(len(mapa)):
       if flag:
         break
       for j in range(len(mapa[i])):
         if navegar.getPadre() != None:
           if navegar.getPadre().getEsferas() != nodo.getEsferas() or navegar.getPadre().getSemillas() != nodo.getSemillas() or navegar.getPadre().getEnemigosEncontrados() != nodo.getEnemigosEncontrados():
             flag = True
             break
           if nodo.getGoku_row() == navegar.getPadre().getGoku_row() and nodo.getGoku_col()-1 == navegar.getPadre().getGoku_col():
             left = False
             #print("no left")
           if nodo.getGoku_row() == navegar.getPadre().getGoku_row() and nodo.getGoku_col()+1 == navegar.getPadre().getGoku_col():
             right = False
             #print("no right")
           if nodo.getGoku_row()-1 == navegar.getPadre().getGoku_row() and nodo.getGoku_col() == navegar.getPadre().getGoku_col():
             up = False
             #print("no up")
           if nodo.getGoku_row()+1 == navegar.getPadre().getGoku_row() and nodo.getGoku_col() == navegar.getPadre().getGoku_col():
             down = False
             #print("no down")
           navegar = navegar.getPadre()
          

     if nodo.getGoku_col() < len(mapa[0])-1 and right:
       if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()+1] != 1 and (nodo.getMovimientoAnterior() != "left" or nodo.getMovimientoAnterior() == "") : #right
           copiaMapa1 = copy.deepcopy(nodo.getMapa())
           nuevoNodo = NodoCosto(nodo, copiaMapa1, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "right")
           nuevoNodo.setEsferas(nodo.getEsferas())
           nuevoNodo.setCosto(nodo.getCosto())
           nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
           nuevoNodo.setSemillas(nodo.getSemillas())
           nuevoNodo.setEnemigosEncontrados(nodo.getEnemigosEncontrados())
           nuevoNodo.move_right()
           colaDeNodos.append(nuevoNodo)

     if nodo.getGoku_col() > 0 and left:
       if nodo.getMapa()[nodo.getGoku_row()][nodo.getGoku_col()-1] != 1 and (nodo.getMovimientoAnterior() != "right" or nodo.getMovimientoAnterior() == ""): #left
           copiaMapa2 = copy.deepcopy(nodo.getMapa())
           nuevoNodo = NodoCosto(nodo, copiaMapa2, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "left")
           nuevoNodo.setEsferas(nodo.getEsferas())
           nuevoNodo.setCosto(nodo.getCosto())
           nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
           nuevoNodo.setSemillas(nodo.getSemillas())
           nuevoNodo.setEnemigosEncontrados(nodo.getEnemigosEncontrados())
           nuevoNodo.move_left()
           colaDeNodos.append(nuevoNodo)

     if nodo.getGoku_row() < len(mapa)-1 and down:
       if nodo.getMapa()[nodo.getGoku_row()+1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "up" or nodo.getMovimientoAnterior() == ""): #down
           copiaMapa3 = copy.deepcopy(nodo.getMapa())
           nuevoNodo = NodoCosto(nodo, copiaMapa3, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "down")
           nuevoNodo.setEsferas(nodo.getEsferas())
           nuevoNodo.setCosto(nodo.getCosto())
           nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
           nuevoNodo.setSemillas(nodo.getSemillas())
           nuevoNodo.setEnemigosEncontrados(nodo.getEnemigosEncontrados())
           nuevoNodo.move_down()
           colaDeNodos.append(nuevoNodo)

     if nodo.getGoku_row() > 0 and up:
       if nodo.getMapa()[nodo.getGoku_row()-1][nodo.getGoku_col()] != 1 and (nodo.getMovimientoAnterior() != "down" or nodo.getMovimientoAnterior() == ""): #up
           copiaMapa4 = copy.deepcopy(nodo.getMapa())
           nuevoNodo = NodoCosto(nodo, copiaMapa4, nodo.getProfundidad()+1, nodo.getGoku_row(), nodo.getGoku_col(), "up")
           nuevoNodo.setEsferas(nodo.getEsferas())
           nuevoNodo.setCosto(nodo.getCosto())
           nuevoNodo.setUltimaCasilla(nodo.getUltimaCasilla())
           nuevoNodo.setSemillas(nodo.getSemillas())
           nuevoNodo.setEnemigosEncontrados(nodo.getEnemigosEncontrados())
           nuevoNodo.move_up()
           colaDeNodos.append(nuevoNodo)

     colaOrdenada = sorted(colaDeNodos, key=NodoCosto.getCosto)
     colaDeNodos = deque(colaOrdenada)
     nodo = colaDeNodos.popleft()
    
     left, right, up, down = True, True, True, True
     flag = False

  solucion = []

# guarda los movimientos optimos para llegar a la solucion.
# contiene desde el último movimiento solución hasta el primer movimiento (sin la raiz)
  while resultado.getPadre() != None:
     solucion.append(resultado.getMapa())
     resultado = resultado.getPadre()
  fin = time.time()
  solucion.append(mapa)
  print("solución registrada")

  return solucion, cantidadDeNodosExpandidos, profundidadFinal, fin - inicio, costoFinal