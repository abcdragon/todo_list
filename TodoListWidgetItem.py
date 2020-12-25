from PyQt5.QtWidgets import QGroupBox, QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QFont

from datetime import datetime


class ResizedQLabel(QLabel):
    def __init__(self, text, font_size, font_family='NanumGothic'):
        super(ResizedQLabel, self).__init__()

        self.font_family = font_family
        self.font_size = font_size

        self.setText(text)
        self.setFont(QFont(self.font_family, self.font_size))

    def set_font(self, font_family, font_size=20):
        self.setFont(QFont(font_family, font_size))


class TodoListWidgetItem(QGroupBox):
    def __init__(self, text):
        super(TodoListWidgetItem, self).__init__()

        self.setLayout(QHBoxLayout())
        self.__todo_label = ResizedQLabel(text, 16)
        self.layout().addWidget(self.__todo_label)
        self.layout().addWidget(QLabel('기간'))

        self.setStyleSheet('''
            QGroupBox {
                border-width: 3px;
                border-style: solid;
            }
        ''')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    qApp = QApplication(sys.argv)
    todolistwidgetitem = TodoListWidgetItem('안녕')
    todolistwidgetitem.show()
    sys.exit(qApp.exec_())
