# coding = UTF-8


# 加载
from PyQt5.QtWidgets import QMainWindow

from widgets.MainWindow.mainwindow import Ui_MainWindow

from widgets.InitWindow.Controller import InitWindow
from utils.initialization import InitThread


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        if True:  # 加载子窗口
            self.__InitWindow = InitWindow()
        if True:  # 加载子线程
            self.__InitThread = InitThread()
        self.__Init()

    def __Init(self):
        self.Space.addWidget(self.__InitWindow)
        self.__InitWindow.show()
        self.__InitThread.FinishFlag.connect(self.__FinishInit)
        self.__InitThread.start()
        return None

    def __FinishInit(self, Message):
        self.__InitWindow.close()
        return None
