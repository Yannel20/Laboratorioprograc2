import  tkinter as tk
from tkinter import *

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Cédula y nombre")
ventana.geometry("600x500")   # Tamaño de la ventana
ventana.config(bg="LightPink1")  # Cambia el color de fondo de la ventana

# Lista para almacenar los datos ingresados
datos_valores = []

def mostrar_datos():
    cedula = DatoCedula.get()
    nombre = DatoNombre.get()
    datos_valores.append(f"Cédula: {cedula}, Nombre: {nombre}")
    
 # Actualizar el botón de resultados con los nuevos datos
    texto_datos = "\n".join(datos_valores)
    boton_resultados.config(text=texto_datos)

# Creamos un Frame para organizar los elementos
miLienzo = tk.Frame(ventana, width=200, height=200, bg="LightPink1")
miLienzo.pack_propagate(False)  # Evita que el frame ajuste su tamaño al contenido
miLienzo.pack(expand=True)  # Expande el frame para centrarlo

# Etiqueta y cuadro de entrada para el Número de Cédula
LabelCedula = tk.Label(miLienzo, text="Cédula:", anchor="w", bg="LightPink1")
LabelCedula.grid(row=0, column=0, padx=10, pady=10, sticky="w")
DatoCedula = tk.Entry(miLienzo, width=50)
DatoCedula.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y cuadro de entrada para el Nombre
LabelNombre = tk.Label(miLienzo, text="Nombre Completo:", anchor="w", bg="LightPink1")
LabelNombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
DatoNombre = tk.Entry(miLienzo, width=50)
DatoNombre.grid(row=1, column=1, padx=10, pady=10)

# Botón para guardar los datos
botonEnviar = tk.Button(miLienzo, text="Guardar datos", command=mostrar_datos)
botonEnviar.grid(row=2, column=1, pady=10, sticky="e")

# Botón para mostrar los resultados
boton_resultados = tk.Button(ventana, text="Aquí podrás ver los datos", wraplength=200, height=2, bg="bisque2")
boton_resultados.pack(padx=10, pady=10, fill="both", expand=True)

ventana.mainloop()