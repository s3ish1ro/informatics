from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QFormLayout, QWidget, QComboBox, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(700, 300, 200, 50)

        cental_widget = QWidget()
        layout = QFormLayout()
        cental_widget.setLayout(layout)
        self.setCentralWidget(cental_widget)

        self.range_label = QLabel('Введите число:')
        self.range_start_input = QLineEdit('1')

        self.message = QMessageBox()
        self.message.setText('привет Миша!')

        self.start_button = QPushButton("Жми! Жми! Жми!")
        self.start_button.clicked.connect(self.f)

        layout.addWidget(self.range_label)
        layout.addWidget(self.range_start_input)
        layout.addWidget(self.start_button)
    def f(self):
        self.message.show()



app = QApplication([])
main_window = MainWindow()
main_window.show()
app.exec()
