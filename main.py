from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import sys
import random
from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.yellow = None
        self.pushButton.clicked.connect(self.DrawRandomCircle)
        self.pushButton_2.clicked.connect(self.DrawYellowCircle)

    def DrawYellowCircle(self):
        self.do_paint = True
        self.yellow = True
        self.repaint()

    def DrawRandomCircle(self):
        self.do_paint = True
        self.yellow = False
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            if self.yellow:
                color = QColor('yellow')
            else:
                color = QColor(random.randint(0, 0xffffff))
            qp.setBrush(color)
            r = random.randint(20, 100)
            w = self.width()
            h = self.height()
            qp.drawEllipse(QPoint(random.randint(r, w - r),
                                  random.randint(r, w - r)), r, r)
            qp.end()
            self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
