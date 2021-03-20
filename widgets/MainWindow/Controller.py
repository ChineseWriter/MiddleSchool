# coding = UTF-8


# 加载
from PyQt5.QtWidgets import QMainWindow

from widgets.MainWindow.mainwindow import Ui_MainWindow

from widgets.InitWindow.Controller import InitWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        if True:
            self.__InitWindow = InitWindow()
        self.__Init()

    def __Init(self):
        self.Space.addWidget(self.__InitWindow)
        self.__InitWindow.show()
        return None
