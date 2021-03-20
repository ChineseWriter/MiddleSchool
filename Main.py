# coding = UTF-8


import sys

from PyQt5.QtWidgets import QApplication

from widgets.MainWindow import MainWindow


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    MainApplication = MainWindow()
    MainApplication.show()
    sys.exit(Application.exec_())
