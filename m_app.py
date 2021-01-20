from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Uncomment if build .exe file in Windows
# try:
#     import pkg_resources.py2_warn
# except ImportError:
#     pass

import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import 

import m_gui as GUI

OS = sys.platform

def main():
    stylesheet = """
        AppWindow {
            background-image: url(image/contour-dark-blue-lines-white.jpg);
            background-repeat: no-repeat;
            background-position: center;
        }
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = GUI.AppWindow(app)
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

