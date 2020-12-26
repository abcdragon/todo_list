from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout

from TodoListWidget import TodoListWidget
from TodoEditWidget import TodoEditWidget


class ErrorBox(QMessageBox):
    def __init__(self, msg):
        super(ErrorBox, self).__init__()
        
        self.setWindowTitle('경고')
        self.setText(msg)
        self.show()
        self.exec_()


class MainView(QWidget):
    def __init__(self):
        super(MainView, self).__init__()

        self.setLayout(QVBoxLayout())

        self.todoedit = TodoEditWidget(lambda: self.func())
        self.layout().addWidget(self.todoedit)

        self.todolist = TodoListWidget()
        self.layout().addWidget(self.todolist)

        self.setFixedSize(500, 750)
        self.setWindowTitle('할 일 목록')
        self.show()

    def func(self):
        try:
            todo = self.todoedit.get_todo()

        except ValueError as e:
            ErrorBox(str(e))

        else:
            self.todolist.add_todo(todo)

        finally:
            self.todoedit.clear_todo_edit()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    qApp = QApplication(sys.argv)
    mainView = MainView()
    sys.exit(qApp.exec_())
