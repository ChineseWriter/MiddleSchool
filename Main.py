# coding = UTF-8


import sys

from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    from widgets.MainWindow import MainWindow
    import Requirements_rc
    MainApplication = MainWindow()
    MainApplication.show()
    sys.exit(Application.exec_())
