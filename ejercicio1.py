from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget)
from PyQt5.Qt import Qt
import sys

class VentanaNombresEdades(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana principal
        self.setWindowTitle("Nombres y Edades")
        self.setGeometry(100, 100, 400, 200)
        
        # Crear el widget central y el layout
        widget_central = QWidget(self)
        layout = QVBoxLayout(widget_central)
        
        # Crear etiquetas de nombre y edad
        self.label_nombre = QLabel("Nombre: Camila Romero", self)
        self.label_edad = QLabel("Edad: 20 años", self)
        
        # Centrar texto en las etiquetas
        self.label_nombre.setAlignment(Qt.AlignCenter)
        self.label_edad.setAlignment(Qt.AlignCenter)
        
        # Añadir las etiquetas al layout
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.label_edad)
        
        # Configurar el widget central
        self.setCentralWidget(widget_central)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaNombresEdades()
    ventana.show()
    sys.exit(app.exec_())
