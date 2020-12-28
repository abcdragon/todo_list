from PyQt5.QtWidgets import QScrollArea, QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt

from TodoListWidgetItem import TodoListWidgetItem


class TodoListWidget(QScrollArea):
    def __init__(self):
        super(TodoListWidget, self).__init__()

        self.todo_lst = QWidget()
        self.todo_lst.setLayout(QVBoxLayout())
        self.todo_lst.layout().setAlignment(Qt.AlignTop)

        self.setWidget(self.todo_lst)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setStyleSheet('background-color:"white"')

    def add_todo(self, text, end_time):
        self.todo_lst.layout().addWidget(TodoListWidgetItem(text, end_time))

    def rmv_todo(self, idx):
        pass
