from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QComboBox)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('График')
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)

        layout.addWidget(self.canvas)

        self.setCentralWidget(cental_widget)

        self.plot_button = QPushButton('Нарисовать график')
        self.plot_button.clicked.connect(self.plot_data)

        self.range_label = QLabel('Диапазон:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')

        self.add_function_button = QPushButton('Добавить функцию в список')
        self.function_input = QLineEdit(' Введите функцию для добавление в список ')
        self.function_widget = QComboBox()
        self.function_widget.addItems(['x', '2*x', 'x**2', 'x**3'])
        self.add_function_button.clicked.connect(self.add_function)

        self.point_amount = QLabel('Количество точек на графике:')
        self.point_input = QLineEdit('50')

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.file_button = QPushButton('Сохранить точки в файл')
        self.file_button.clicked.connect(self.file_save)

        layout.addWidget(self.function_widget)
        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.range_end_input)
        layout.addWidget(self.point_amount)
        layout.addWidget(self.point_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.file_button)
        layout.addRow(self.add_function_button, self.function_input)

    def vectors(self):
        try:
            expression = self.function_widget.currentText()
        except NameError:
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
        try:
            exec(f'def f(x): return {expression}', functions)
        except SyntaxError:
            exec(f'def f(x): return x', functions)

        x = np.linspace(range_start, range_end, points)
        function = functions['f']
        try:
            y = [function(value) for value in x]
        except NameError:
            y = [value for value in x]

        return x, y

    def plot_data(self):

        x, y = self.vectors()
        axes = plt.subplot()
        axes.plot(x, y)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')

        self.centralWidget().layout().itemAt(0).widget().draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        plt.grid(True)
        self.canvas.draw()

    def file_save(self):
        x, y = self.vectors()
        file = open('dots.txt', 'w')
        file.write('x     ' + '  ' + 'y\n')
        for i in range(len(x)):
            a, b = map(str, (x[i], y[i]))
            a, b = a[0:6], b[0:6]
            if len(a) < 6:
                a += '0' * (6 - len(a))
            if len(b) < 6:
                b += '0' * (6 - len(b))
            file.write(a + '  ' + b + '\n')

    def add_function(self):
        text_x = self.function_input.text()
        self.function_widget.addItems([text_x])


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()
