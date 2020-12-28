from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout

from ResizedQLabel import ResizedQLabel


class TodoListWidgetItem(QGroupBox):
    def __init__(self, text, end_time):
        super(TodoListWidgetItem, self).__init__()

        self.setLayout(QHBoxLayout())
        self.__todo_label = ResizedQLabel(text)
        self.layout().addWidget(self.__todo_label)
        self.layout().addStretch(1)
        self.layout().addWidget(ResizedQLabel('| 기간:', 10))
        self.layout().addWidget(ResizedQLabel(end_time, 10))

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
    todolistwidgetitem = TodoListWidgetItem('안녕', '2020-12-27')
    todolistwidgetitem.show()
    sys.exit(qApp.exec_())
