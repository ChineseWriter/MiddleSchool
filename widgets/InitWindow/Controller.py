# coding = UTF-8


from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QMovie, QPixmap

from widgets.InitWindow.initwindow import Ui_InitWindow


class InitWindow(Ui_InitWindow, QWidget):
    def __init__(self, parent=None):
        super(InitWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.__ShowInitPic()

    def __ShowInitPic(self):
        Loading_GIF = QMovie(":/images/assets/images/Loading.gif")
        self.label.setMovie(Loading_GIF)
        Loading_GIF.start()
        return None
