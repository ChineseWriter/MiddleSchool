# coding = UTF-8


from PyQt5.QtWidgets import QWidget

from widgets.MusicWindow.music import Ui_MusicWindow

from ini.Style import WindowColor


class MusicWindow(Ui_MusicWindow, QWidget):
    def __init__(self, parent=None):
        super(MusicWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    def Render(self):
        if WindowColor == "Black":
            with open("./assets/qss/MusicWindow/black.css", "r", encoding="UTF-8") as File:
                Text = File.read()
            self.setStyleSheet(Text)
            self.LocalMusic.setText("本地音乐")
            self.DownloadManage.setText("下载管理")
        return None
