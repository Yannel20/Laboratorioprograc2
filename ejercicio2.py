
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QPushButton, QLineEdit, QVBoxLayout, QLabel)

import sys

class URSS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setGeometry(100, 100, 400, 200) 
        self.setWindowTitle("Ventana de Clave Secreta")
        
        # Crear un widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Etiqueta de instrucciones
        self.label_instrucciones = QLabel("Ingresa el mensaje, nosotros lo codificamos en idioma que esta sifrado:", self)

        # Campo de entrada para el mensaje
        self.entrada_datos = QLineEdit(self)
        self.entrada_datos.setEchoMode(QLineEdit.Password)  # Ocultar entrada como contraseña

        # Botón para enviar los datos
        self.boton_enviar = QPushButton("Enviar", self)
        self.boton_enviar.clicked.connect(self.verClave)

        # Etiqueta para mostrar el mensaje codificado
        self.label_codificado = QLabel("", self)

        # Disposición vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_instrucciones)
        layout.addWidget(self.entrada_datos)
        layout.addWidget(self.boton_enviar)
        layout.addWidget(self.label_codificado)

        # Configuración de la ventana
        central_widget.setLayout(layout)
        self.setWindowTitle("Ventana de Incognito")
        self.show()

    def verClave(self):
        # Leer el texto del campo de entrada
        mensaje = self.entrada_datos.text()
        mensaje_codificado = self.codificar_mensaje(mensaje)

        # Mostrar el mensaje codificado en la etiqueta
        self.label_codificado.setText(f"Tu mensaje a sido codificado en idioma sifrado es: {mensaje_codificado}")

    def codificar_mensaje(self, mensaje):
        # Simulación de una codificación en sifrado (solo convierte vocales en guiones y puntos como ejemplo)
        traduccion = {'a': '.-', 'e': '.', 'i': '..', 'o': '---', 'u': '..-'}
        mensaje_codificado = ''.join([traduccion.get(letra, letra) for letra in mensaje.lower()])
        return mensaje_codificado


# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = URSS()
    ventana.show()
    sys.exit(app.exec_())
