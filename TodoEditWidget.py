from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from ResizedQLabel import ResizedQLabel

from re import fullmatch


class GetTermDialog(QDialog):
    def __init__(self):
        super(GetTermDialog, self).__init__()

        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle('종료 날짜 입력')
        self.setLayout(QVBoxLayout())
        self.__init_ui()

    def __init_ui(self):
        info_box = QGroupBox('종료 날짜')
        info_box.setLayout(QVBoxLayout())

        info_box.layout().addWidget(ResizedQLabel('년-월-일:', 14))

        input_layout = QHBoxLayout()
        self.__ymd = [QLineEdit(), ResizedQLabel(' - ', 12), QLineEdit(), ResizedQLabel(' - ', 12), QLineEdit()]
        for idx, widget in enumerate(self.__ymd):
            if idx % 2 == 0:
                widget.setFont(QFont('NanumGothic', 12))
                widget.setMaxLength(4 if idx == 0 else 2)

            input_layout.addWidget(widget)

        self.__ymd = self.__ymd[::2]
        info_box.layout().addLayout(input_layout)

        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        btn_box.accepted.connect(self.__ok)
        btn_box.rejected.connect(self.__reject)

        self.layout().addWidget(info_box)
        self.layout().addWidget(btn_box)

    def get_end_time(self):
        if [0 for e in self.__ymd if not e.text()] and self.__success:
            raise ValueError('모든 칸을 입력해주세요')

        return '-'.join([e.text() for e in self.__ymd]) if self.__success else None

    def __ok(self):
        self.__success = True
        self.close()

    def __reject(self):
        self.__success = False
        self.close()


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
