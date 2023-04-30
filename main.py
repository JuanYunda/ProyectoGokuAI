import tkinter as tk
from busqueda_amplitud import busqueda_amplitud
import time
from PIL import Image, ImageTk
import easygui as eg
import numpy as np

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
        time.sleep(1)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Mapa")

# Crear el canvas para dibujar el mapa
CELL_SIZE = 50
canvas = tk.Canvas(ventana, width=500, height=500, bg='gray')
canvas.pack()

# Cargar las imágenes que deseas mostrar en la interfaz
img_camino = Image.open('camino.png') #camino
img_muro = Image.open('muro.png') #paredes
img_goku = Image.open('goku.png') #goku
img_freezer = Image.open('freezer.png') #freezer
img_cell = Image.open('cell.png') #cell
img_semilla = Image.open('semilla.png') #semilla
img_esfera = Image.open('esfera.png') #esfera
    
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

def busqueda_anchura():
    global solucion
    solucion = busqueda_amplitud(matrizInicial)
    imprimir()
    
"""def busqueda_profundidad():
    global solucion
    solucion = buscar_camino_profundidad()
    
def busqueda_costo_uniforme():
    global solucion
    solucion = buscar_camino_costo_uniforme()
    
def busqueda_a_estrella():
    global solucion
    solucion = buscar_camino_a_estrella()
    
def busqueda_voraz():
    global solucion
    solucion = buscar_camino_voraz()"""

# Función para crear los botones
def crear_botones():
    botones = tk.Frame(ventana)
    botones.pack(side='bottom', pady=10)

    btn_anchura = tk.Button(botones, text='Búsqueda en Anchura', command=busqueda_anchura)
    btn_anchura.pack(side='left', padx=5)
    
    """btn_profundidad = tk.Button(botones, text='Búsqueda en Profundidad', command=busqueda_profundidad)
    btn_profundidad.pack(side='left', padx=5)
    
    btn_costo_uniforme = tk.Button(botones, text='Búsqueda con Costo Uniforme', command=busqueda_costo_uniforme)
    btn_costo_uniforme.pack(side='left', padx=5)
    
    btn_a_estrella = tk.Button(botones, text='Búsqueda A*', command=busqueda_a_estrella)
    btn_a_estrella.pack(side='left', padx=5)
    
    btn_voraz = tk.Button(botones, text='Búsqueda Voraz', command=busqueda_voraz)
    btn_voraz.pack(side='left', padx=5)"""

# Llamar a la función para crear los botones

solucion = []

archivo = eg.fileopenbox(msg='Seleccione el mapa',
                        title='Seleccion de mapa',
                        multiple=False,
                        )
     
mapa = open(archivo, 'r')
matrizInicial = np.loadtxt(mapa, dtype='i', delimiter=' ')

draw_map(canvas, matrizInicial)
crear_botones()

for i in range(len(images)-1):
    images.pop(i)

# Mostrar la ventana
print("finalizado")
ventana.mainloop()
