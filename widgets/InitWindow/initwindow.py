# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InitWindow(object):
    def setupUi(self, InitWindow):
        InitWindow.setObjectName("InitWindow")
        InitWindow.resize(676, 512)
        self.horizontalLayout = QtWidgets.QHBoxLayout(InitWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(InitWindow)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(InitWindow)
        QtCore.QMetaObject.connectSlotsByName(InitWindow)

    def retranslateUi(self, InitWindow):
        _translate = QtCore.QCoreApplication.translate
        InitWindow.setWindowTitle(_translate("InitWindow", "Form"))
