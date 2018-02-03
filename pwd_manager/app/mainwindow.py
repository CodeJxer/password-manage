# -*- coding=UTF-8 -*-
#
# Copyright © pwd-manager Project Contributors
# Licensed under the terms of the MIT License
# (see pwd-manager/__init__.py for details)

# Stdlib imports
import sys

# Local imports

# Qt imports
from PyQt4 import QtGui, QtCore

class pwd_Manager(QtGui.QMainWindow):
    def __init__(self):
        super(pwd_Manager, self).__init__()

        self.initUI()

    def initUI(self):
        pass


def main():
    app = QtGui.QApplication([])
    pwd_manager = pwd_Manager()
    pwd_manager.show()
    app.exec_()


if __name__ == '__main__':
    main()
