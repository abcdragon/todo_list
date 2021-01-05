from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtCore import Qt

from ResizedQLabel import ResizedQLabel

from re import fullmatch
from datetime import datetime


class CustomedQLineEdit(QWidget):
    def __init__(self, obj_name):
        super(CustomedQLineEdit, self).__init__()

        self.setLayout(QHBoxLayout())

        self.__edit = QLineEdit()
        self.__edit.setObjectName(obj_name)
        self.__edit.setValidator(QIntValidator())
        self.__edit.setFont(QFont('NanumGothic', 12))
        self.__edit.setMaxLength(4 if obj_name == 'year' else 2)
        self.__edit.setText(str(eval('datetime.today().' + str(obj_name))))
        self.layout().addWidget(self.__edit)

        self.layout().addWidget(ResizedQLabel({'year': '년', 'month': '월', 'day': '일',
                                               'hour': '시', 'minute': '분'}[obj_name].center(3)))

    def connect(self, func):
        self.__edit.textChanged.connect(func)

    def text(self):
        return self.__edit.text()


class GetTermDialog(QDialog):
    def __init__(self):
        super(GetTermDialog, self).__init__()

        self.__success = False
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle('종료 날짜 입력')
        self.setLayout(QVBoxLayout())
        self.__init_ui()

    def __init_ui(self):
        info_box = QGroupBox('종료 날짜')
        info_box.setLayout(QVBoxLayout())

        self.btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.btn_box.accepted.connect(self.__ok)
        self.btn_box.rejected.connect(self.__reject)

        self.btn_box.buttons()[0].setText('확인')
        self.btn_box.buttons()[1].setText('취소')

        self.__in_widget = [[CustomedQLineEdit(name) for name in names] for names in [['year', 'month', 'day'], ['hour', 'minute']]]

        for widgets in self.__in_widget:
            layout = QHBoxLayout()
            for widget in widgets:
                widget.connect(self.date_chk)
                layout.addWidget(widget)

            info_box.layout().addLayout(layout)

        self.layout().addWidget(info_box)
        self.layout().addWidget(self.btn_box)

    def date_chk(self):
        enable = False
        try:
            in_day = [int(s) if s and s != '0' else 1 for s in [e.text() for w in self.__in_widget for e in w]]
            in_day = datetime(year=in_day[0], month=in_day[1], day=in_day[2],
                              hour=in_day[3], minute=in_day[4])
            today = datetime.today()
            now = datetime(year=today.year, month=today.month, day=today.day,
                           hour=today.hour, minute=today.minute)
            enable = now <= in_day
            
        except ValueError:
            pass

        finally:
            self.btn_box.buttons()[0].setEnabled(enable)

    def get_end_time(self):
        if [0 for w in self.__in_widget for e in w if not e.text()] and self.__success:
            raise ValueError('모든 칸을 입력해주세요')

        return '-'.join(['%02d' % int(e.text()) for w in self.__in_widget for e in w]) if self.__success else None

    def __ok(self):
        self.__success = True
        self.close()

    def __reject(self):
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
