from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QRadioButton, QButtonGroup, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon
import sys

class Restaurante(QMainWindow):
    def __init__(self):
        super(Restaurante, self).__init__()

        # Configuración de la ventana principal
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Restaurante Caramon')
        
        # Cambiar el color de fondo
        fondocolor = QPalette()
        fondocolor.setColor(QPalette.Window, QColor(219, 145, 225))
        self.setPalette(fondocolor)

        # Crear el widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Crear etiquetas y campos de entrada
        self.label_comida = QLabel('Costo de la comida:')
        self.inNombre_2 = QLineEdit(self)  # Campo para el costo de la comida

        self.label_bebida = QLabel('Costo de la bebida:')
        self.inBebida = QLineEdit(self)  # Campo para el costo de la bebida

        # Radio buttons para aplicar descuento
        self.radioSinDescuento = QRadioButton('Sin descuento')
        self.radioConDescuento = QRadioButton('Con descuento (10%)')
        
        # Agrupar los radio buttons
        self.radioGroup = QButtonGroup(self)
        self.radioGroup.addButton(self.radioSinDescuento)
        self.radioGroup.addButton(self.radioConDescuento)
        self.radioSinDescuento.setChecked(True)  # Por defecto, sin descuento

        # Campo de salida para mostrar el precio final
        self.label_precioFinal = QLabel('Precio Final:')
        self.txtPrecioFinal = QLineEdit(self)
        self.txtPrecioFinal.setReadOnly(True)  # Campo solo de lectura

        # Botón para calcular el precio final
        self.btnCalcular = QPushButton('Calcular Precio Final')
        self.btnCalcular.clicked.connect(self.calcularPrecioFinal)

        # Layouts para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_comida)
        layout.addWidget(self.inNombre_2)
        layout.addWidget(self.label_bebida)
        layout.addWidget(self.inBebida)
        layout.addWidget(self.radioSinDescuento)
        layout.addWidget(self.radioConDescuento)
        layout.addWidget(self.label_precioFinal)
        layout.addWidget(self.txtPrecioFinal)
        layout.addWidget(self.btnCalcular)

        # Configuración del layout principal
        central_widget.setLayout(layout)

    def calcularPrecioFinal(self):
  
        try:
            # Obtener los valores de los campos y asegurarse de que sean numéricos
            costo_comida = float(self.inNombre_2.text()) if self.inNombre_2.text() else 0.0
            costo_bebida = float(self.inBebida.text()) if self.inBebida.text() else 0.0
            
            # Calcular el precio base
            precioFinal = costo_comida + costo_bebida
            
            # Verificar si el radio button de "Con descuento" está activado
            if self.radioConDescuento.isChecked():
                precioFinal *= 0.9  # Aplicar un 10% de descuento

            # Mostrar el resultado en el campo de precio final
            self.txtPrecioFinal.setText(f"{precioFinal:.2f}")  # Mostrar el número con 2 decimales
            
        except ValueError:
            # En caso de que no se pueda convertir el texto en número, mostrar un mensaje de error
            self.txtPrecioFinal.setText("Los valores deben ser numerico")


# Inicialización de la aplicación
app = QApplication(sys.argv)
ventana = Restaurante()
ventana.show()
sys.exit(app.exec_())


