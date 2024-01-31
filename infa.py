from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')

        self.canvas = FigureCanvas(plt.figure())

        cental_widget = QWidget()
        layout = QVBoxLayout()
        cental_widget.setLayout(layout)

        layout.addWidget(self.canvas)

        self.setCentralWidget(cental_widget)

        self.plot_button = QPushButton('Нарисовать график')
        self.plot_button.clicked.connect(self.plot_data)

        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')

        self.function_label = QLabel('Функция:')
        self.function_input = QLineEdit('x**3')

        self.point_amount = QLabel('Количество точек на графике:')
        self.point_input = QLineEdit('50')

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear)

        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.range_end_input)
        layout.addWidget(self.point_amount)
        layout.addWidget(self.point_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.clear_button)
    def plot_data(self):

        try:
            expression = self.function_input.text()
        except ValueError:
            expression = 'x'


        try:
            range_start = float(self.range_start_input.text())
            range_end = float(self.range_end_input.text())
            points = int(self.point_input.text())
        except ValueError:
            range_start = 0
            range_end = 1
            points = 50

        functions = {}
        exec(f'def f(x): return {expression}', functions)

        x = np.linspace(range_start, range_end, points)
        function = functions['f']

        y = [function(value) for value in x]

        plt.plot(x, y)
        plt.grid(True)

        plt.xlabel('x')
        plt.ylabel('y')

        plt.title('График y = ' + expression)

        self.centralWidget().layout().itemAt(0).widget().draw()

    def clear(self):
        self.plt.clf()


app = QApplication([])
main_window = MainWindow()
main_window.show()

app.exec()
