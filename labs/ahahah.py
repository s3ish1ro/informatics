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

        self.plot_button = QPushButton('Проверить точку')
        self.plot_button.clicked.connect(self.plot_scatter)

        self.range_label = QLabel('Введите координату точки:')
        self.range_start_input = QLineEdit('0')
        self.range_end_input = QLineEdit('1')
        self.range_start_input.setFixedSize(50, 25)
        self.range_end_input.setFixedSize(50, 25)
        self.clear_button = QPushButton('Очистить график')
        self.clear_button.clicked.connect(self.clear_plot)

        layout.addRow(self.range_label)
        layout.addRow(self.range_start_input, self.range_end_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.clear_button)
        self.plot_data()

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
        plt.title('Task 4')
        self.canvas.draw()

    def plot_scatter(self):
        def check1(x, y):
            """
            функция проверяет попадает ли точка в левую заданную область с помощью уравнений,
            так же для удобства область поделена на 2 части(полуокружность и многоугольник)
            """
            r = 2
            if (x + 1) ** 2 + (y - 3) ** 2 <= r ** 2 and x < -1:
                return True
            elif x >= -1 and -1.5 * (x - 1) + 2 >= y >= 3 * x - 1 and y >= -2 * x - 1:
                return True
            else:
                return False

        def check2(x, y):
            """
            функция проверяет попадает ли точка в правую заданную область с помощью уравнений,
            так же для удобства область поделена на 3 части(полуокружность, параллелограмм и треугольник)
            """
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
        x, y = map(float, [self.range_start_input.text(), self.range_end_input.text()])
        if check1(x, y):
            plt.scatter(x, y, color='green')
        elif check2(x, y):
            plt.scatter(x, y, color='green')
        else:
            plt.scatter(x, y, color='red')
        self.canvas.draw()

    def clear_plot(self):
        for ax in self.fig.axes:
            ax.clear()
        self.plot_data()



app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()
