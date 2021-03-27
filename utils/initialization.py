# coding = UTF-8


import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from utils.threading import Thread
from ini import Style


class InitThread(Thread):
    FinishFlag = pyqtSignal(str)

    def __init__(self, MainWindow: QMainWindow):
        super(InitThread, self).__init__()
        self.MainWindow = MainWindow

    def run(self):
        time.sleep(1)
        self.DoSomething()
        self.FinishFlag.emit("Finish")
        return None

    def DoSomething(self):
        if Style.WindowColor == "Black":
            with open("./assets/qss/black.css", "r", encoding="UTF-8") as File:
                Text = File.read()
            self.MainWindow.setStyleSheet(Text)
            self.MainWindow.setWindowOpacity(Style.WindowTransparency)
        if Style.WindowColor == "White":
            with open("./assets/qss/white.css", "r", encoding="UTF-8") as File:
                Text = File.read()
            self.MainWindow.setStyleSheet(Text)
            self.MainWindow.setWindowOpacity(Style.WindowTransparency)
