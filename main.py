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


class calc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.ui.btn_del_one_element.clicked.connect(self.clean_label)

        self.ui.btn_dot.clicked.connect(self.dot)

        self.ui.btn_plus.clicked.connect(self.add_mem)

        self.ui.btn_plus.clicked.connect(self.math_operations)
        self.ui.btn_minus.clicked.connect(self.math_operations)
        self.ui.btn_multiply.clicked.connect(self.math_operations)
        self.ui.btn_divide.clicked.connect(self.math_operations)
        self.ui.btn_degree.clicked.connect(self.math_operations)

    def add_digit(self):
        btn = self.sender()
        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')
        if btn.objectName() in digit_buttons:
            if self.ui.lineEdit.text() == '0':
                self.ui.lineEdit.setText(btn.text())
            else:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn.text())

    def clean_all(self):
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()

    def clean_label(self):
        self.ui.lineEdit.setText('0')

    def dot(self):
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')

    def add_mem(self):
        btn = self.sender()
        entry = self.del_zero(self.ui.lineEdit.text())
        if not self.ui.label.text():
            self.ui.label.setText(entry + f'{btn.text()}')
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
        if self.ui.lineEdit.text():
            return self.ui.label.text().strip('.').split()[-1]

    def calculate(self):
        entry = self.ui.lineEdit.text()
        temp = self.ui.label.text()
        if temp:
            result = self.del_zero(str(
                operation[self.get_sign()](self.get_num_lineedit(), self.get_num_label())))
            self.ui.lineEdit.setText(temp + self.del_zero(entry) + '=')
            self.ui.lineEdit.setText(result)
            return result

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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = calc()
    window.show()
    sys.exit(app.exec())
