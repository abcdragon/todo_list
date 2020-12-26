from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QFont

from ResizedQLabel import ResizedQLabel

from re import fullmatch


class TodoEditWidget(QWidget):
    def __init__(self, btn_func):
        super(TodoEditWidget, self).__init__()

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(ResizedQLabel('할 일: '))

        self.__todo_edit = QLineEdit()
        self.__todo_edit.setFont(QFont('NanumGothic', 16))
        self.layout().addWidget(self.__todo_edit)

        button = QPushButton('추가하기')
        button.setFont(QFont('NanumGothic', 16))
        button.clicked.connect(btn_func)
        self.layout().addWidget(button)

    def get_todo(self):
        text = self.__todo_edit.text()

        if not fullmatch('[a-zA-Z가-힣+].*', text):
            raise ValueError('할 일을 입력해주세요')

        return text

    def clear_todo_edit(self):
        self.__todo_edit.clear()
