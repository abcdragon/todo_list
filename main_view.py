from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from TodoListWidget import TodoListWidget


class MainView(QWidget):
    def __init__(self):
        super(MainView, self).__init__()

        main_layout = QVBoxLayout()
        #main_layout.addStretch(1)

        self.todolist = TodoListWidget()
        main_layout.addWidget(self.todolist)

        button = QPushButton('버튼')
        button.clicked.connect(self.func)

        main_layout.addWidget(button)

        self.setLayout(main_layout)

        self.setFixedSize(500, 750)
        self.setWindowTitle('할 일 목록')
        self.show()

    def func(self):
        self.todolist.add_todo('안녕하세요')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    qApp = QApplication(sys.argv)
    mainView = MainView()
    sys.exit(qApp.exec_())
