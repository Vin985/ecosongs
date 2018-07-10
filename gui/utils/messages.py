from PySide2.QtWidgets import QMessageBox

# Type of icons available:
# Warning
# Critical
# Information
# Question


def showMessage(text, type):
    msgBox = QMessageBox()
    msgBox.setText(text)
    msgBox.setIcon(type)
    return (msgBox.exec_())


def showAlert(text):
    showMessage(text, QMessageBox.Critical)


def showInfo(text):
    showMessage(text, QMessageBox.Info)


def showWarning(text):
    showMessage(text, QMessageBox.Warning)


def showConfirmBox(text, info):
    msgBox = QMessageBox()
    msgBox.setText(text)
    msgBox.setInformativeText(info)
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Ok)
    return (msgBox.exec_())
