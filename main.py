from PyQt6 import QtWidgets
import sys


class calc(QtWidgets.QWidget):
    def __init__(self):
        super(calc, self).__init__()
        self.setWindowTitle('calculator')
        self.my_layout = QtWidgets.QGridLayout()
        self.setLayout(self.my_layout)

        self.btn_0 = QtWidgets.QPushButton('0')
        self.btn_1 = QtWidgets.QPushButton('1')
        self.btn_2 = QtWidgets.QPushButton('2')
        self.btn_3 = QtWidgets.QPushButton('3')
        self.btn_4 = QtWidgets.QPushButton('4')
        self.btn_5 = QtWidgets.QPushButton('5')
        self.btn_6 = QtWidgets.QPushButton('6')
        self.btn_7 = QtWidgets.QPushButton('7')
        self.btn_8 = QtWidgets.QPushButton('8')
        self.btn_9 = QtWidgets.QPushButton('9')
        self.btn_plus = QtWidgets.QPushButton('+')
        self.btn_minus = QtWidgets.QPushButton('-')
        self.btn_clean = QtWidgets.QPushButton('CE')
        self.btn_multiply = QtWidgets.QPushButton('*')
        self.btn_divide = QtWidgets.QPushButton('/')
        self.btn_percent = QtWidgets.QPushButton('%')
        self.btn_equals = QtWidgets.QPushButton('=')
        self.btn_dot = QtWidgets.QPushButton('.')
        self.btn_sign = QtWidgets.QPushButton('+/-')
        self.btn_degree = QtWidgets.QPushButton('^')
        self.answer = QtWidgets.QLabel('')

        self.my_layout.addWidget(self.answer, 0, 0, 1, 4)
        self.my_layout.addWidget(self.btn_0, 5, 1)
        self.my_layout.addWidget(self.btn_1, 4, 0)
        self.my_layout.addWidget(self.btn_2, 4, 1)
        self.my_layout.addWidget(self.btn_3, 4, 2)
        self.my_layout.addWidget(self.btn_4, 3, 0)
        self.my_layout.addWidget(self.btn_5, 3, 1)
        self.my_layout.addWidget(self.btn_6, 3, 2)
        self.my_layout.addWidget(self.btn_7, 2, 0)
        self.my_layout.addWidget(self.btn_8, 2, 1)
        self.my_layout.addWidget(self.btn_9, 2, 2)
        self.my_layout.addWidget(self.btn_plus, 1, 3)
        self.my_layout.addWidget(self.btn_minus, 2, 3)
        self.my_layout.addWidget(self.btn_clean, 1, 2)
        self.my_layout.addWidget(self.btn_multiply, 3, 3)
        self.my_layout.addWidget(self.btn_divide, 4, 3)
        self.my_layout.addWidget(self.btn_percent, 1, 1)
        self.my_layout.addWidget(self.btn_equals, 5, 3)
        self.my_layout.addWidget(self.btn_dot, 5, 0)
        self.my_layout.addWidget(self.btn_sign, 5, 2)
        self.my_layout.addWidget(self.btn_degree, 1, 0)







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = calc()
    window.show()
    sys.exit(app.exec())
