from PyQt6 import QtWidgets
import sys


class calc(QtWidgets.QWidget):
    def __init__(self):
        super(calc, self).__init__()
        self.setWindowTitle('calculator')
        self.my_layout = QtWidgets.QGridLayout()
        self.setLayout(self.my_layout)
        self.value = ''
        self.operator = ''
        self.num = 0

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

        self.btn_1.clicked.connect(self.one)
        self.btn_2.clicked.connect(self.two)
        self.btn_3.clicked.connect(self.three)
        self.btn_4.clicked.connect(self.four)
        self.btn_5.clicked.connect(self.five)
        self.btn_6.clicked.connect(self.six)
        self.btn_7.clicked.connect(self.seven)
        self.btn_8.clicked.connect(self.eight)
        self.btn_9.clicked.connect(self.nine)
        self.btn_0.clicked.connect(self.zero)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_clean.clicked.connect(self.clean)
        self.btn_multiply.clicked.connect(self.multiply)
        self.btn_divide.clicked.connect(self.divide)
        self.btn_percent.clicked.connect(self.percent)
        self.btn_equals.clicked.connect(self.equals)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_sign.clicked.connect(self.sign)
        self.btn_degree.clicked.connect(self.degree)

    def plus(self):
        self.num = float(self.value)
        self.operator = '+'
        self.value = self.value + '+'
        self.answer.setText('{}'.format(str(self.value).rstrip('.0')))

    def minus(self):
        self.num = float(self.value)
        self.operator = '-'
        self.value = self.value + '-'
        self.answer.setText('{}'.format(self.value))

    def clean(self):
        self.num = 0
        self.operator = ''
        self.value = ''
        self.answer.setText('{}'.format(self.value))

    def multiply(self):
        self.num = float(self.value)
        self.operator = '*'
        self.value = self.value + '*'
        self.answer.setText('{}'.format(self.value))

    def divide(self):
        self.num = float(self.value)
        self.operator = '/'
        self.value = self.value + '/'
        self.answer.setText('{}'.format(self.value))

    def percent(self):
        self.num = float(self.value)
        self.operator = '%'
        self.value = self.value + '%'
        self.answer.setText('{}'.format(self.value))

    def degree(self):
        self.num = float(self.value)
        self.operator = '^'
        self.value = self.value + '^'
        self.answer.setText('{}'.format(self.value))

    def sign(self):
        self.num = float(self.value)
        new_sign = self.num * (-1)
        self.value = new_sign
        self.answer.setText('{}'.format(str(new_sign).rstrip('.0')))

    def dot(self):
        self.value = self.value + '.'
        self.answer.setText('{}'.format(self.value))

    # def sender(self):
    #    pass

    '''def add_digit(self):
        btn = self.sender()
        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')
        if btn.objectName() in digit_buttons:
            if self.answer.text() == '0':
                self.answer.setText(btn.text())
            else:
                self.answer.setText(self.answer.text() + btn.text())'''

    def one(self):
        self.value = self.value + '1'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def two(self):
        self.value = self.value + '2'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def three(self):
        self.value = self.value + '3'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def four(self):
        self.value = self.value + '4'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def five(self):
        self.value = self.value + '5'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def six(self):
        self.value = self.value + '6'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def seven(self):
        self.value = self.value + '7'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def eight(self):
        self.value = self.value + '8'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def nine(self):
        self.value = self.value + '9'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def zero(self):
        self.value = self.value + '0'
        self.answer.setText('{}'.format(self.value))
        print(self.value)

    def equals(self):
        value_2 = self.value
        if self.operator == '+':
            x = float((value_2.split('+')[1]))
            y = float(self.num) + x
            self.answer.setText('{}'.format(str(y).rstrip('.0')))
            self.value = str(y).rstrip('.0')
        elif self.operator == '-':
            x = float((value_2.split('-')[1]))
            y = float(self.num) - x
            self.answer.setText('{}'.format(str(y).rstrip('.0')))
            self.value = str(y).rstrip('.0')
        elif self.operator == '*':
            x = float((value_2.split('*')[1]))
            y = float(self.num) * x
            self.answer.setText('{}'.format(str(y).rstrip('.0')))
            self.value = str(y).rstrip('.0')
        elif self.operator == '^':
            x = float((value_2.split('^')[1]))
            y = float(self.num) ** x
            self.answer.setText('{}'.format(str(y).rstrip('.0')))
            self.value = str(y).rstrip('.0')
        elif self.operator == '/':
            try:
                x = float((value_2.split('/')[1]))
                y = float(self.num) / x
                self.answer.setText('{}'.format(str(y).rstrip('.0')))
                self.value = str(y).rstrip('.0')
            except ZeroDivisionError:
                self.answer.setText('Division by 0 not allowed!')
                self.num = ''
                self.value = ''
        '''elif self.operator == '%':
            x = float((value_2.split('-' or '+')[1]))
            # y = float(self.num) * x
            # self.answer.setText('{}'.format(y))
            # self.value = str(y)
            print('x', x, 'type', type(x))'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = calc()
    window.show()
    sys.exit(app.exec())
