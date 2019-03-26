import sys
from PyQt5 import QtGui, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setGeometry(100, 100, 480, 360)
    window.setWindowTitle('Main window')
    window.show()
    ret_code = app.exec_()
    sys.exit(ret_code)

if __name__ == '__main__':
    main()
