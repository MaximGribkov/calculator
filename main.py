from PyQt6 import QtWidgets
import sys
from design import Ui_MainWindow
from operator import add, sub, mul, truediv, pow

operation = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '^': pow
}

dev_zero_error = 'Division by zero'
undefined_error = 'Result is undefined'


class calc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.max_len = self.ui.lineEdit.maxLength()

        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)
        self.ui.btn_0.clicked.connect(self.add_digit)

        self.ui.btn_clear.clicked.connect(self.clean_all)
        self.ui.btn_del_one_element.clicked.connect(self.backspace)

        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_sign.clicked.connect(self.negation)

        self.ui.btn_plus.clicked.connect(self.math_operations)
        self.ui.btn_minus.clicked.connect(self.math_operations)
        self.ui.btn_multiply.clicked.connect(self.math_operations)
        self.ui.btn_divide.clicked.connect(self.math_operations)
        self.ui.btn_degree.clicked.connect(self.math_operations)
        self.ui.btn_equals.clicked.connect(self.calculate)

    def add_digit(self):
        btn = self.sender()
        self.del_error()
        self.clear_label_equals()
        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')
        if btn.objectName() in digit_buttons:
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(btn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text())

    def clean_all(self):
        self.del_error()
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()

    def backspace(self):
        self.del_error()
        entry = self.ui.lineEdit.text()
        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.lineEdit.setText('0')
            else:
                self.ui.lineEdit.setText(entry[:-1])
        else:
            self.ui.lineEdit.setText('0')

    def dot(self):
        self.clear_label_equals()
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')

    def add_mem(self):
        btn = self.sender()
        entry = self.del_zero(self.ui.lineEdit.text())
        if not self.ui.label.text() or self.get_sign() == '=':
            self.ui.label.setText(entry + f' {btn.text()}')
            self.ui.lineEdit.setText('0')

    @staticmethod
    def del_zero(num):
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def get_num_lineedit(self):
        entry = self.ui.lineEdit.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_num_label(self):
        if self.ui.label.text():
            temp = self.ui.label.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_sign(self):
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]

    def calculate(self):
        entry = self.ui.lineEdit.text()
        temp = self.ui.label.text()
        if temp:
            try:
                result = self.del_zero(str(
                    operation[self.get_sign()](self.get_num_label(), self.get_num_lineedit())))
                self.ui.label.setText(temp + self.del_zero(entry) + ' =')
                self.ui.lineEdit.setText(result)
                return result
            except KeyError:
                pass
            except ZeroDivisionError:
                if self.get_num_label() == 0:
                    self.show_error(undefined_error)
                else:
                    self.show_error(dev_zero_error)

    def math_operations(self):
        temp = self.ui.label.text()
        btn = self.sender()
        if not temp:
            self.add_mem()
        else:
            if self.get_sign() != btn.text():
                if self.get_sign() == '=':
                    self.add_mem()
                else:
                    self.ui.label.setText(temp[:-2] + f'{btn.text()}')
            else:
                try:
                    self.ui.label.setText(self.calculate() + f'{btn.text()}')
                except TypeError:
                    pass

    def negation(self):
        entry = self.ui.lineEdit.text()
        self.clear_label_equals()
        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]
        if len(entry) == self.max_len + 1 and '-' in entry:
            self.ui.lineEdit.setMaxLength(self.max_len + 1)
        else:
            self.ui.lineEdit.setMaxLength(self.max_len)
        self.ui.lineEdit.setText(entry)

    def clear_label_equals(self):
        if self.get_sign() == '=':
            self.ui.label.clear()

    def show_error(self, text):
        self.ui.lineEdit.setMaxLength(len(text))
        self.ui.lineEdit.setText(text)

    def del_error(self):
        if self.ui.lineEdit.text() in (dev_zero_error, undefined_error):
            self.ui.lineEdit.setMaxLength(self.max_len)
            self.ui.lineEdit.setText('0')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = calc()
    window.show()
    sys.exit(app.exec())
