import tkinter as tk
import easygui
from busqueda_amplitud import busqueda_amplitud
from busqueda_profundidad import busqueda_profundidad
from busqueda_AStar import busqueda_A_Star
from busqueda_Avara import busqueda_Avara
from busqueda_costo import busqueda_costo
import time
from PIL import Image, ImageTk
import easygui as eg
import numpy as np
from busqueda_costo import busqueda_costo 

#ProyectoGokuAI
#Elaborado por:
#Mauricio Carrillo - 2024092
#Juan Esteban Mazuera - 2043008
#Sheilly Ortega - 2040051

botones = None
flag = True
global tipo_busqueda

# Función para dibujar el mapa en la ventana
def draw_map(canvas, map_data):
    images = {
    0: img_camino,
    1: img_muro,
    2: img_goku,
    3: img_freezer,
    4: img_cell,
    5: img_semilla,
    6: img_esfera,
    }
    
    # Dibujar cada celda en el canvas con el color correspondiente
    filas = len(map_data)
    colum = len(map_data[0])
    for row_idx in range(filas):
        for col_idx in range(colum):
            x1 = col_idx * CELL_SIZE
            y1 = row_idx * CELL_SIZE
            canvas.create_image(x1, y1, image=images[int(map_data[row_idx][col_idx])], anchor='nw')

# Función para ejecutar la búsqueda correspondiente
def imprimir():
    # Actualizar el ciclo for para que recorra la lista de soluciones
    for i in reversed(solucion):
        # Definir el mapa que se desea mostrar
        map_data = i

        # Dibujar el mapa en el canvas
        draw_map(canvas, map_data)
        ventana.update()
        time.sleep(0.5)

def busqueda_anchura():
    global solucion
    global flag
    global etiqueta_costo
    solucion, nodosExpandidos, profundidadFinal, tiempo = busqueda_amplitud(matrizInicial)
    if flag:
        if etiqueta_costo is not None:
            etiqueta_costo.destroy()
        etiqueta_costo = None
        flag = False
    actualizarValoresSinCosto(nodosExpandidos, profundidadFinal, tiempo)
    imprimir()

    
def busqueda_de_profundidad():
    global solucion
    global flag
    global etiqueta_costo
    solucion, nodosExpandidos, profundidadFinal, tiempo = busqueda_profundidad(matrizInicial)
    if flag:
        if etiqueta_costo is not None:
            etiqueta_costo.destroy()  # Eliminar el Label existente
        etiqueta_costo = None
        flag = False
    actualizarValoresSinCosto(nodosExpandidos, profundidadFinal, tiempo)
    imprimir()
    
def busqueda_costo_uniforme():
    global solucion
    global etiqueta_costo
    global flag
    solucion, nodosExpandidos, profundidadFinal, tiempo, costo = busqueda_costo(matrizInicial)
    if not flag:
        if etiqueta_costo is not None:
            etiqueta_costo.config(text='Costo de la solución: ' + str(costo))
        else:
            etiqueta_costo = tk.Label(ventana, text='Costo de la solución: ')
            etiqueta_costo.pack()
        flag = True
    actualizarValores(nodosExpandidos, profundidadFinal, tiempo, costo)
    imprimir()
    
def busqueda_a_estrella():
    global solucion
    global etiqueta_costo
    global flag
    solucion, nodosExpandidos, profundidadFinal, tiempo, costo = busqueda_A_Star(matrizInicial)
    if not flag:
        if etiqueta_costo is not None:
            etiqueta_costo.config(text='Costo de la solución: ' + str(costo))
        else:
            etiqueta_costo = tk.Label(ventana, text='Costo de la solución: ')
            etiqueta_costo.pack()
        flag = True
    actualizarValores(nodosExpandidos, profundidadFinal, tiempo, costo)
    imprimir()
  
def busqueda_avara():
    global solucion
    global etiqueta_costo
    global flag
    solucion, nodosExpandidos, profundidadFinal, tiempo = busqueda_Avara(matrizInicial)
    if flag:
        if etiqueta_costo is not None:
            etiqueta_costo.destroy()  # Eliminar el Label existente
        etiqueta_costo = None
        flag = False
    actualizarValoresSinCosto(nodosExpandidos, profundidadFinal, tiempo)
    imprimir()

# Actualizar los valores de las etiquetas (sin costo)
def actualizarValoresSinCosto(expand, prof, tiem):
    etiqueta_nodos.config(text='Nodos expandidos: ' + str(expand))
    etiqueta_profundidad.config(text='Profundidad de la solución: ' + str(prof))
    etiqueta_tiempo.config(text='Tiempo de la solución: ' + str(tiem))
    
# Actualizar los valores de las etiquetas
def actualizarValores(expand, prof, tiem, cost):
    etiqueta_nodos.config(text='Nodos expandidos: ' + str(expand))
    etiqueta_profundidad.config(text='Profundidad de la solución: ' + str(prof))
    etiqueta_tiempo.config(text='Tiempo de la solución: ' + str(tiem))
    etiqueta_costo.config(text='Costo de la solución: ' + str(cost))

def cargar_mapa():
    global matrizInicial
    global solucion

    archivo = eg.fileopenbox(msg='Seleccione el nuevo mapa',
                            title='Seleccion de mapa',
                            multiple=False)

    mostrar_interfaz()
    crear_botones()

    if archivo is not None:
        mapa = open(archivo, 'r')
        matrizInicial = np.loadtxt(mapa, dtype='i', delimiter=' ')
        mapa.close()

        # Limpiar la solución anterior
        solucion = []

        # Dibujar el nuevo mapa en el lienzo
        draw_map(canvas, matrizInicial)

        # Actualizar la interfaz
        ventana.update()

# Función para crear los botones
def crear_botones():
    global botones

    if botones is not None:
        botones.destroy()
        botones = None
        
    botones = tk.Frame(ventana)
    botones.pack(side='bottom', pady=10)

    if tipo_busqueda:
        btn_a_estrella = tk.Button(botones, text='Búsqueda A*', command=busqueda_a_estrella)
        btn_a_estrella.pack(side='left', padx=5)
    
        btn_voraz = tk.Button(botones, text='Búsqueda Avara', command=busqueda_avara)
        btn_voraz.pack(side='left', padx=5)

    else:
        btn_anchura = tk.Button(botones, text='Búsqueda por Amplitud', command=busqueda_anchura)
        btn_anchura.pack(side='left', padx=5)
    
        btn_costo_uniforme = tk.Button(botones, text='Búsqueda con Costo Uniforme', command=busqueda_costo_uniforme)
        btn_costo_uniforme.pack(side='left', padx=5)

        btn_profundidad = tk.Button(botones, text='Búsqueda en Profundidad', command=busqueda_de_profundidad)
        btn_profundidad.pack(side='left', padx=5)

def cerrar_programa():
    ventana.destroy()

# Función para cambiar el valor de la variable booleana global
def cambiar_variable(valor):
    global tipo_busqueda
    tipo_busqueda = valor

# Función para mostrar la interfaz flotante
def mostrar_interfaz():
    respuesta = easygui.buttonbox("Seleccione el tipo de busqueda a realizar:", choices=["Busqueda Informada", "Busqueda No Informada"])
    if respuesta == "Busqueda Informada":
        cambiar_variable(True)
    else:
        cambiar_variable(False)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mapa")
ventana.resizable(False, False)  # Desactivar la redimensión de la ventana
# Cambiar el color de fondo de la ventana a azul
ventana.configure(bg="white")

# Crear el contenedor para los botones
contenedor_botones = tk.Frame(ventana)
contenedor_botones.pack(side='top', padx=5, pady=5)
# Boton "Cargar Nuevo Mapa"
btn_cargar_mapa = tk.Button(contenedor_botones, text='Cargar Nuevo Mapa', command=cargar_mapa, bg="gray")
btn_cargar_mapa.pack(side='left', padx=(0, 200))
# Crear el botón "Cerrar"
btn_cerrar = tk.Button(contenedor_botones, text="Cerrar", command=cerrar_programa, bg="red")
btn_cerrar.pack(side="left", padx=(200, 0))


# Crear el canvas para dibujar el mapa
CELL_SIZE = 50
canvas = tk.Canvas(ventana, width=500, height=500, bg='gray')
canvas.pack()

# Cargar las imágenes que deseas mostrar en la interfaz
img_camino = Image.open('images/camino.png') #camino
img_muro = Image.open('images/muro.png') #paredes
img_goku = Image.open('images/goku.png') #goku
img_freezer = Image.open('images/freezer.png') #freezer
img_cell = Image.open('images/cell.png') #cell
img_semilla = Image.open('images/semilla.png') #semilla
img_esfera = Image.open('images/esfera.png') #esfera
    
# Escalar las imágenes a la dimensión de las celdas
img_camino = img_camino.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_muro = img_muro.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_goku = img_goku.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_freezer = img_freezer.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_cell = img_cell.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_semilla = img_semilla.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
img_esfera = img_esfera.resize((CELL_SIZE, CELL_SIZE), Image.LANCZOS)
    
# Convertir las imágenes a un formato compatible con tkinter
img_camino = ImageTk.PhotoImage(img_camino)
img_muro = ImageTk.PhotoImage(img_muro)
img_goku = ImageTk.PhotoImage(img_goku)
img_freezer = ImageTk.PhotoImage(img_freezer)
img_cell = ImageTk.PhotoImage(img_cell)
img_semilla = ImageTk.PhotoImage(img_semilla)
img_esfera = ImageTk.PhotoImage(img_esfera)

# Definir las imagenes para cada valor en el mapa
images = {
    0: img_camino,
    1: img_muro,
    2: img_goku,
    3: img_freezer,
    4: img_cell,
    5: img_semilla,
    6: img_esfera,
}

# Crear etiquetas para mostrar los valores
etiqueta_nodos = tk.Label(ventana, text='Nodos expandidos: ')
etiqueta_nodos.pack()
etiqueta_profundidad = tk.Label(ventana, text='Profundidad de la solución: ')
etiqueta_profundidad.pack()
etiqueta_tiempo = tk.Label(ventana, text='Tiempo de la solución: ')
etiqueta_tiempo.pack()
etiqueta_costo = tk.Label(ventana, text='Costo de la solución: ')
etiqueta_costo.pack()

solucion = []

mostrar_interfaz()
crear_botones()

archivo = eg.fileopenbox(msg='Seleccione el mapa',
                        title='Seleccion de mapa',
                        multiple=False,
                        )
     
mapa = open(archivo, 'r')
matrizInicial = np.loadtxt(mapa, dtype='i', delimiter=' ')

draw_map(canvas, matrizInicial)

for i in range(len(images)-1):
    images.pop(i)

# Mostrar la ventana
print("finalizado")
ventana.mainloop()
