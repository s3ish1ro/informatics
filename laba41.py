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
        self.plot_button.clicked.connect(self.plot_scatter)

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
        self.higherlower.addItem('higher', 'lower')

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('k'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('степень x'))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem('b'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem('выше/ниже'))
        self.table.setCellWidget(0, 3, self.higherlower)

        self.ff = QPushButton('Нарисовать кривую')
        self.ff.clicked.connect(self.plot_data1)
        layout.addRow(self.scatter_label)
        layout.addRow(self.scatter_start_input, self.scatter_end_input)
        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addWidget(self.ff)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.clear_button)
        layout.addRow(self.table)



    def plot_data(self):
        theta = np.linspace(np.pi / 2, 3 * np.pi / 2, 150)

        radius = 2

        a1 = radius * np.cos(theta) - 1
        b1 = radius * np.sin(theta) + 3
        x1 = [-1, 1, 0, -1]
        y1 = [5, 2, -1, 1]
        axes = plt.subplot()
        axes.plot(a1, b1, color='black')
        axes.plot(x1, y1, color='black')
        axes.set_aspect(1)

        theta2 = np.linspace(np.pi, 2 * np.pi, 150)
        radius = 2

        a2 = radius * np.cos(theta2) + 4
        b2 = radius * np.sin(theta2) - 1
        x2 = [2, 3, 2, 7, 6]
        y2 = [-1, 0, 1, 0, -1]
        axes.plot(x2, y2, color='black')
        axes.plot(a2, b2, color='black')
        plt.grid(True)
        plt.title('Task 1')
        self.canvas.draw()

    def plot_scatter(self):
        def check1(x, y):

            pass

        def check2(x, y):
            r = 2
            if y < -1 and (x - 4) ** 2 + (y + 1) ** 2 == r ** 2:
                return True
            # упрощенное условие -1 <= y <= 0 and y <= x - 3 and y >= x - 7
            elif -1 <= y <= x - 3 and x - 7 <= y <= 0:
                return True
            # упрощенное условие y >= 0 and y >= -x + 3 and y <= -0.2 * x + 1.4
            elif 0 < y <= (-2 * x + 14) / 10 and y >= -x + 3:
                return True
            else:
                return False
        x, y = map(float, [self.scatter_start_input.text(), self.scatter_end_input.text()])
        if check1(x, y):
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
        if self.vectors_line() != 0:
            x, y = self.vectors_line()
            axes = plt.subplot()
            axes.plot(x, y)
            plt.grid(True)
            plt.xlabel('x')
            plt.ylabel('y')

            self.centralWidget().layout().itemAt(0).widget().draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        self.canvas.draw()


app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()
