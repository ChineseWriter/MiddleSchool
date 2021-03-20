# coding = UTF-8


from utils.threading import Thread

from PyQt5.QtCore import pyqtSignal

import time


class InitThread(Thread):
    FinishFlag = pyqtSignal(str)

    def __init__(self):
        super(InitThread, self).__init__()

    def run(self):
        time.sleep(3)
        self.FinishFlag.emit("Finish")
        return None
