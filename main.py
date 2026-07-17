from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi  


import sys
from utils.paths import resource_path



# UI forms loaded inside application
MAIN_WINDOW = resource_path('ui', 'designer', 'main.ui')


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		loadUi(str(MAIN_WINDOW), self)
		self.setGeometry(200,200,1100,700)
		icon_path = resource_path('ui', 'designer', 'icons', 'shield.png')
		self.setWindowIcon(QIcon(str(icon_path)))
		



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())



