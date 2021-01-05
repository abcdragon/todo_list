from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


def template_font(font_size=14, font_family='NanumGhothic'):
    return QFont(font_family, font_size)


class ResizedQLabel(QLabel):
    def __init__(self, text, font_size=14, font_family='NanumGothic'):
        super(ResizedQLabel, self).__init__()

        self.font_family = font_family
        self.font_size = font_size

        self.setText(text)
        self.setFont(QFont(self.font_family, self.font_size))

    def set_font(self, font_family, font_size=14):
        self.setFont(QFont(font_family, font_size))
