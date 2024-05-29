import random
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QTableWidgetItem, QTableWidget, QComboBox)
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

        self.plot_button = QPushButton('Проверить точку')
        self.plot_button.clicked.connect(self.check2)

        self.scatter_label = QLabel('Введите координату точки:')
        self.scatter_start_input = QLineEdit('0')
        self.scatter_end_input = QLineEdit('1')
        self.scatter_start_input.setFixedSize(50, 25)
        self.scatter_end_input.setFixedSize(50, 25)

        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        self.range_label = QLabel('Введите диапазон фукнции:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')
        self.range_start_input.setFixedSize(50, 25)
        self.range_end_input.setFixedSize(50, 25)

        self.higherlower = QComboBox()
        self.higherlower.addItems(['выше', 'ниже'])

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('k'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('степень x'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('b'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('выше/ниже'))
        self.table.setCellWidget(0, 3, self.higherlower)
        self.start_button = QPushButton('Нарисовать кривую')
        self.start_button.clicked.connect(self.plot_data1)

        self.random_button = QPushButton("Случайная точка")
        self.random_button.clicked.connect(self.random_choice)
        self.vectors_x = []
        layout.addRow(self.scatter_label)
        layout.addRow(self.scatter_start_input, self.scatter_end_input)
        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.random_button)
        layout.addRow(self.table)

    def check1(self, x, y, k, n, b, hl):
        k, n, b = map(float, (k, n, b))
        if hl == 'выше':
            return y >= k * x**n + b
        else:
            return y <= k * x**n + b

    def check2(self):
        x, y = map(float, [self.scatter_start_input.text(), self.scatter_end_input.text()])
        count = 0
        number = len(self.vectors_x)
        for koofs in self.vectors_x:
            if self.check1(x, y, koofs[0], koofs[1], koofs[2], koofs[3]):
                count += 1
        if count == number:
            plt.scatter(x, y, color='blue')
        elif count >= 1:
            plt.scatter(x, y, color='green')
        else:
            plt.scatter(x, y, color='red')
        self.canvas.draw()

    def vectors_line(self):
        k = self.table.item(0, 0).text()
        n = self.table.item(0, 1).text()
        b = self.table.item(0, 2).text()
        expression = f'{k} * x**({n}) + ({b})'
        try:
            range_start, range_end = map(float, (self.range_start_input.text(), self.range_end_input.text()))
            x = np.linspace(range_start, range_end, 50)
            functions = {}
            exec(f'def f(x): return {expression}', functions)
            function = functions['f']
            y = [function(value) for value in x]
            return x, y
        except SyntaxError:
            return 0
        except NameError:
            return 0

    def plot_data1(self):
        hl = str(self.table.cellWidget(0, 3).currentText())
        k = self.table.item(0, 0).text()
        n = self.table.item(0, 1).text()
        b = self.table.item(0, 2).text()
        self.vectors_x.append([k, n, b, hl])
        if self.vectors_line() != 0:
            x, y = self.vectors_line()
            axes = plt.subplot()
            axes.plot(x, y, color='black')
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')
            self.centralWidget().layout().itemAt(0).widget().draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        self.vectors_x = []
        self.canvas.draw()

    def random_choice(self):
        a = str(random.uniform(-5, 5))[0:4]
        b = str(random.uniform(-5, 5))[0:4]
        self.scatter_start_input.setText(a)
        self.scatter_end_input.setText(b)
        self.check2()

app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()
