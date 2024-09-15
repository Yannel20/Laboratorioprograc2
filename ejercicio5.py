import tkinter as tk
from tkinter import * 

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Describiendo a una persona")
ventana.geometry("600x600")   # Tamaño de la ventana
ventana.config(bg="DarkOliveGreen1")  # Cambia el color de fondo de la ventana

# Función para mostrar los datos 
def mostrar_datos():
    datos = [entrada.get() for entrada in entradas]
    texto_datos = "\n".join([f"{datos_valores[i]}: {dato}" for i, dato in enumerate(datos)])
    
    # Creamos un botón dinámico con los datos ingresados
    boton_resultados.config(text=texto_datos)

# Creamos un Frame principal para organizar los elementos
miLienzo = tk.Frame(ventana, bg="DarkOliveGreen1")  # Aplicamos el color de fondo al Frame
miLienzo.pack(expand=True, fill='both')

# Creamos un Frame interno para centrar los elementos
frameCentro = tk.Frame(miLienzo, bg="DarkOliveGreen1")  # Se aplica el color de fondo al Frame
frameCentro.pack(expand=True)

# Etiquetas y botones para los datos
datos_valores = [
    "Nombre",
    "Género",
    "Edad",
    "Estatura",
    "Ocupación",
    "Estado civil",
    "Color de ojos",
    "Complexión física",
    "Hobbies",
    "Comida favorita"
]

entradas = []

for i, nombre in enumerate(datos_valores):
    # Crea y coloca el label en la columna 0
    label = tk.Label(frameCentro, text=nombre, bg="lightgrey")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
    
    # Crea y coloca el cuadro de entrada en la columna 1
    entrada = tk.Entry(frameCentro, width=30)  # Ajustar el ancho
    entrada.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
    entradas.append(entrada)

# Botón para enviar los datos
botonEnviar = tk.Button(frameCentro, text="Registrar datos", command=mostrar_datos, bg="salmon1")
botonEnviar.grid(row=len(datos_valores), column=1, pady=10, sticky="e")

# Botón para mostrar los resultados
boton_resultados = tk.Button(frameCentro, text="En este apartado aparecerán los datos", wraplength=500, height=10, bg="bisque2")
boton_resultados.grid(row=len(datos_valores) + 1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Configura el peso de las columnas y filas para centrar los elementos
frameCentro.grid_columnconfigure(0, weight=1)
frameCentro.grid_columnconfigure(1, weight=2)
frameCentro.grid_rowconfigure(len(datos_valores), weight=1)

ventana.mainloop()