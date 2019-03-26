import sys
from PyQt5 import QtGui, QtWidgets

import interface

def main():
    # Create a Qt Application
    app = QtWidgets.QApplication(sys.argv)

    # Create a window and draw it
    window = interface.create_gui()
    window.show()

    # Run the Qt application and return any potential error codes
    ret_code = app.exec_()
    sys.exit(ret_code)

if __name__ == '__main__':
    main()
