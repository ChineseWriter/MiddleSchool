# coding = UTF-8


import time

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QMainWindow

from utils.threading import Thread
from ini import Style


class InitThread(Thread):
    FinishFlag = pyqtSignal(str)

    def __init__(self, MainWindow: QMainWindow):
        super(InitThread, self).__init__()
        self.MainWindow = MainWindow

    def run(self):
        self.DoSomething()
        time.sleep(1)
        self.FinishFlag.emit("Finish")
        return None

    def DoSomething(self):
        if Style.WindowColor == "Black":
            with open("./assets/qss/MainWindow/black.css", "r", encoding="UTF-8") as File:
                Text = File.read()
        elif Style.WindowColor == "White":
            with open("./assets/qss/MainWindow/white.css", "r", encoding="UTF-8") as File:
                Text = File.read()
        else:
            Text = ""
        self.MainWindow.setStyleSheet(Text)
        self.MainWindow.setWindowOpacity(Style.WindowTransparency)
        # self.MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        # self.MainWindow.setWindowFlag(Qt.FramelessWindowHint)
