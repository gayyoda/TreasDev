from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def Window():
    app = QApplication
    win = QMainWindow()
    win.setGeometry(0, 0, 1000, 1000)
    win.setWindowTitle("AAC Board")
    win.show()
    sys.exit(app.exec_())
Window()