from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class CommonUIUtils(object):
    @staticmethod
    def showWarningMessageBox(text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.exec_()

    @staticmethod
    def showSuccessMessage(text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QMessageBox.NoIcon)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()