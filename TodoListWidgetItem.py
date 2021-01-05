from PyQt5.QtWidgets import QGroupBox, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout

from ResizedQLabel import ResizedQLabel, template_font


class TodoListWidgetItem(QGroupBox):
    def __init__(self, text, end_time):
        super(TodoListWidgetItem, self).__init__()

        self.setLayout(QHBoxLayout())
        self.__todo_label = ResizedQLabel(text)
        self.__todo_label.mouseDoubleClickEvent = self.todo_double_clicked
        self.layout().addWidget(self.__todo_label)
        self.layout().addStretch(1)
        self.layout().addWidget(ResizedQLabel('| 기간:', font_size=10))
        self.layout().addWidget(ResizedQLabel(end_time, font_size=10))

        self.setStyleSheet('''
            QGroupBox {
                border-width: 3px;
                border-style: solid;
            }
        ''')

    def todo_double_clicked(self, event):
        self.layout().removeWidget(self.__todo_label)
        self.__todo_label.deleteLater()
        self.__todo_label = QLineEdit(self.__todo_label.text())
        self.__todo_label.focusOutEvent = self.focus_out
        self.__todo_label.setFont(template_font())
        self.layout().insertWidget(0, self.__todo_label)
        self.__todo_label.setFocus()

    def focus_out(self, event):
        self.layout().removeWidget(self.__todo_label)
        self.__todo_label.deleteLater()
        self.__todo_label = ResizedQLabel(self.__todo_label.text())
        self.__todo_label.mouseDoubleClickEvent = self.todo_double_clicked
        self.layout().insertWidget(0, self.__todo_label)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    qApp = QApplication(sys.argv)
    todolistwidgetitem = TodoListWidgetItem('안녕', '2020-12-27')
    todolistwidgetitem.show()
    sys.exit(qApp.exec_())
