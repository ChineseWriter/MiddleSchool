# coding = UTF-8


from PyQt5.QtWidgets import QWidget

from widgets.MusicWindow.music import Ui_MusicWindow


class MusicWindow(Ui_MusicWindow, QWidget):
    def __init__(self, parent=None):
        super(MusicWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)