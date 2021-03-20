# coding = UTF-8


from PyQt5.QtCore import QThread


class Thread(QThread):
    def __init__(self):
        super(Thread, self).__init__()

    def kill(self):
        self.terminate()
