from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Window import StartWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    print("программа запущена")
    sys.exit(app.exec_())