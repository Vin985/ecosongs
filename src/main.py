if __name__ == "__main__":
    print("using main")
    import sys
    from ecosongs import Ecosongs
    from gui.ecosongsUI import EcosongsUI

    app = Ecosongs(sys.argv)

    # f = QFile("gui/resources/qss/custom.qss")
    # f.open(QFile.ReadOnly)
    # res = QTextStream(f).readAll()
    # print(res)
    # app.setStyleSheet(res)
    ui = EcosongsUI()  # We set the form to be our ExampleApp (design)
    ui.showMaximized()
    sys.exit(app.exec_())
