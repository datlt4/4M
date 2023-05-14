from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Uncomment if build .exe file in Windows
try:
    import pkg_resources.py2_warn
except ImportError:
    pass

import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import m_database as DB
import m_gui as GUI

database_path = "./Minh_s_expense.db"

OS = sys.platform

def main():
    stylesheet = """
        AppWindow {
            background-image: url(image/contour-dark-blue-lines-white.jpg);
            background-repeat: no-repeat;
            background-position: center;
        }
    """
    conn = DB.ConnectDatabase("Minh_s_expense.db")
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(lambda: print("__Application exited__"))
    app.setStyleSheet(stylesheet)
    window = GUI.AppWindow(app, conn)
    # window.showFullScreen()
    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

