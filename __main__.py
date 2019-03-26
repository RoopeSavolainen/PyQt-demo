import sys
from PyQt5 import QtGui, QtWidgets

import interface

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = interface.create_gui()
    window.show()
    ret_code = app.exec_()
    sys.exit(ret_code)

if __name__ == '__main__':
    main()
