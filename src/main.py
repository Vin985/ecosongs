from PySide2.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    # f = QFile("gui/resources/qss/custom.qss")
    # f.open(QFile.ReadOnly)
    # res = QTextStream(f).readAll()
    # print(res)
    # app.setStyleSheet(res)
    ui = Ecosongs()  # We set the form to be our ExampleApp (design)
    ui.showMaximized()
    sys.exit(app.exec_())
