import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # importamos Pillow ya que deseo insertar una imagen en tkinter

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Datos de Mascotas")
ventana.geometry("600x600")   # Tamaño de la ventana
ventana.config(bg="coral")  # Cambia el color de fondo de la ventana

# Creamos un marco para centrar el contenido y cambiar su color de fondo
marco = tk.Frame(ventana, bg="coral")
marco.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el marco en la ventana

# Cargar y redimensionar la imagen
img = Image.open("mascot.png")     # Nos aseguramos de que la imagen esté en el mismo directorio que el script
img = img.resize((200, 200))       # Ajustamos el tamaño 
img_tk = ImageTk.PhotoImage(img)   # Convertir la imagen para tkinter

# Creamos un label con la imagen y centrarlo en el marco
lbl_img = tk.Label(marco, image=img_tk, bg="coral")
lbl_img.grid(row=0, column=0, columnspan=2, pady=10)

def mostrar_datos():
    mascota1 = f"Mascota 1 - Nombre: {entry_nombre1.get()}, Edad: {entry_edad1.get()} años, Peso: {entry_peso1.get()} libras"
    mascota2 = f"Mascota 2 - Nombre: {entry_nombre2.get()}, Edad: {entry_edad2.get()} años, Peso: {entry_peso2.get()} libras"
    mascota3 = f"Mascota 3 - Nombre: {entry_nombre3.get()}, Edad: {entry_edad3.get()} años, Peso: {entry_peso3.get()} libras"
    
 # Mostrar los datos en el botón de resultados
    boton_resultados.config(text=f"{mascota1}\n{mascota2}\n{mascota3}")

# Etiquetas y entradas para la mascota 1
tk.Label(marco, text="Mascota 1", bg="coral").grid(row=1, column=0, columnspan=2, pady=(20, 5))
tk.Label(marco, text="Nombre:", bg="coral").grid(row=2, column=0, sticky="e")
entry_nombre1 = tk.Entry(marco, width=20)
entry_nombre1.grid(row=2, column=1)

tk.Label(marco, text="Edad:", bg="coral").grid(row=3, column=0, sticky="e")
entry_edad1 = tk.Entry(marco, width=20)
entry_edad1.grid(row=3, column=1)

tk.Label(marco, text="Peso (libras):", bg="coral").grid(row=4, column=0, sticky="e")
entry_peso1 = tk.Entry(marco, width=20)
entry_peso1.grid(row=4, column=1)

# Etiquetas y entradas para la mascota 2
tk.Label(marco, text="Mascota 2", bg="coral").grid(row=5, column=0, columnspan=2, pady=(20, 5))
tk.Label(marco, text="Nombre:", bg="coral").grid(row=6, column=0, sticky="e")
entry_nombre2 = tk.Entry(marco, width=20)
entry_nombre2.grid(row=6, column=1)

tk.Label(marco, text="Edad:", bg="coral").grid(row=7, column=0, sticky="e")
entry_edad2 = tk.Entry(marco, width=20)
entry_edad2.grid(row=7, column=1)

tk.Label(marco, text="Peso (libras):", bg="coral").grid(row=8, column=0, sticky="e")
entry_peso2 = tk.Entry(marco, width=20)
entry_peso2.grid(row=8, column=1)

# Etiquetas y entradas para la mascota 3
tk.Label(marco, text="Mascota 3", bg="coral").grid(row=9, column=0, columnspan=2, pady=(20, 5))
tk.Label(marco, text="Nombre:", bg="coral").grid(row=10, column=0, sticky="e")
entry_nombre3 = tk.Entry(marco, width=20)
entry_nombre3.grid(row=10, column=1)

tk.Label(marco, text="Edad:", bg="coral").grid(row=11, column=0, sticky="e")
entry_edad3 = tk.Entry(marco, width=20)
entry_edad3.grid(row=11, column=1)

tk.Label(marco, text="Peso (libras):", bg="coral").grid(row=12, column=0, sticky="e")
entry_peso3 = tk.Entry(marco, width=20)
entry_peso3.grid(row=12, column=1)

# Botón para mostrar los datos
boton_mostrar = tk.Button(marco, text="Enviar Datos", command=mostrar_datos, bg="salmon1")
boton_mostrar.grid(row=13, column=0, columnspan=2, pady=10)

# Botón para mostrar los resultados
boton_resultados = tk.Button(marco, text="Aquí aparecerán los datos", wraplength=500, height=10, bg="bisque2")
boton_resultados.grid(row=14, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

ventana.mainloop()
