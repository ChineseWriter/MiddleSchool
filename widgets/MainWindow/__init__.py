# coding = UTF-8


from PyQt5.QtWidgets import QMainWindow

from widgets.MainWindow.mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
