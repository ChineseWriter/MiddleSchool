# coding = UTF-8


# 加载
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from widgets.MainWindow.mainwindow import Ui_MainWindow

from widgets.InitWindow.Controller import InitWindow
from widgets.MusicWindow.Controller import MusicWindow
from utils.initialization import InitThread


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        if True:  # 加载子窗口
            self.__InitWindow = InitWindow(self)
            self.__MusicWindow = MusicWindow(self)
            self.__InitWindow.close()
            self.__MusicWindow.close()
        if True:
            self.OpenMusicManager.triggered.connect(self.__OpenMusicManager)
        if True:  # 加载子线程
            self.__InitThread = InitThread(self)
        self.__Init()


    def __Init(self):
        self.setWindowTitle("加载中")
        self.setWindowIcon(QIcon(":/images/assets/images/logo1.png"))
        self.StatusBar.showMessage("加载中 . . .")
        self.Space.addWidget(self.__InitWindow)
        self.__InitWindow.show()
        self.__InitThread.FinishFlag.connect(self.__FinishInit)
        self.__InitThread.start()
        return None

    def __FinishInit(self, Message):
        self.StatusBar.clearMessage()
        self.setWindowTitle("青春纪念册")
        self.__InitWindow.close()
        self.__RemoveWindow()
        return None

    def __RemoveWindow(self):
        for Index in range(self.Space.count()):
            self.Space.removeWidget(self.Space.itemAt(Index).widget())
        return None

    def __OpenMusicManager(self):
        self.__RemoveWindow()
        self.Space.addWidget(self.__MusicWindow)
        self.__MusicWindow.show()
        self.__MusicWindow.Render()
        return None
