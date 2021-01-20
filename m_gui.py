import sys
import os
from functools import partial
from PyQt5.QtCore import Qt, QRect, QTimer, QThread, QThreadPool, QRunnable, QObject, pyqtSignal, pyqtSlot, QSize
from PyQt5.QtWidgets import QComboBox, QMainWindow, QVBoxLayout, QHBoxLayout, QMessageBox, QProgressBar
from PyQt5.QtWidgets import QLabel, QFileDialog, QLineEdit, QFrame, QMenu, QInputDialog, QSpacerItem
from PyQt5.QtWidgets import QApplication, QAction, qApp, QGroupBox, QRadioButton, QSizePolicy, QFrame
from PyQt5.QtWidgets import QTabWidget, QWidget, QPushButton, QListWidget, QGridLayout, QStackedWidget
from PyQt5.QtWidgets import QDialog, QListWidgetItem
from PyQt5.QtGui import QColor, QFont, QPixmap, QIcon, QImage, QPainter, QPen
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLineSeries, QBarSet, QPercentBarSeries, QBarCategoryAxis
from uuid import uuid4

OS = sys.platform
username = "Minh Nguyen"
avatar = "image/avatar.png"

if OS.startswith("win32"):
    # FONT = FONT
    FONT = "Noah"
elif OS.startswith("linux"):
    FONT = "Serif"
elif OS.startswith("darwin"):
    FONT = "Serif"
else:
    sys.exit(1)

def currency(value, currency_symbol="VND", brief=False, round_to_decimal=True):
    if brief:
        _v = len(str(int(value)))
        if (_v > 0) and (_v < 6):
            return "{:,.2f}K {}".format(value/1e3, currency_symbol)
        elif (_v >= 6 ) and (_v < 9):
            return "{:,.2f}M {}".format(value/1e6, currency_symbol)
        else:
            return "{:,.2f}B {}".format(value/1e9, currency_symbol)
    else:
        if round_to_decimal:
            return "{:,} {}".format(round(value), currency_symbol)
        elif not round_to_decimal and not brief:
            return "{:,.2f} {}".format(value, currency_symbol)

class MFont():
    def __init__(self):
        self.font10B = QFont();
        self.font10U = QFont();
        self.font10BI = QFont();
        self.font12 = QFont();
        self.font12B = QFont();
        self.font12U = QFont();
        self.font14 = QFont();
        self.font14B = QFont();
        self.font15B = QFont();
        self.font16 = QFont();
        self.font16B = QFont();
        self.font16U = QFont();
        self.font16BU = QFont();
        self.font18 = QFont();
        self.font18B = QFont();
        self.font18U = QFont();
        self.font18BU = QFont();
        self.font20 = QFont();
        self.font20B = QFont();
        self.font20I = QFont();
        self.font20U = QFont();
        self.font20UB = QFont();
        self.font24 = QFont();
        self.font24B = QFont();
        self.font24BU = QFont();
        self.font30B = QFont();
        self.font30BU = QFont();
        self.define()
    
    def define(self):
        self.font10B.setFamily(FONT);
        self.font10B.setPointSize(10);
        self.font10B.setBold(True);

        self.font10U.setFamily(FONT);
        self.font10U.setPointSize(10);
        self.font10U.setUnderline(True);

        self.font10BI.setFamily(FONT);
        self.font10BI.setPointSize(10);
        self.font10BI.setItalic(True);
        self.font10BI.setBold(True);

        self.font12.setFamily(FONT);
        self.font12.setPointSize(12);

        self.font12B.setFamily(FONT);
        self.font12B.setPointSize(12);
        self.font12B.setBold(True);

        self.font12U.setFamily(FONT);
        self.font12U.setPointSize(12);
        self.font12U.setUnderline(True);

        self.font14.setFamily(FONT);
        self.font14.setPointSize(14);

        self.font14B.setFamily(FONT);
        self.font14B.setPointSize(14);
        self.font14B.setBold(True);

        self.font15B.setFamily(FONT);
        self.font15B.setPointSize(15);
        self.font15B.setBold(True);

        self.font16.setFamily(FONT);
        self.font16.setPointSize(16);

        self.font16B.setFamily(FONT);
        self.font16B.setPointSize(16);
        self.font16B.setBold(True);

        self.font16U.setFamily(FONT);
        self.font16U.setPointSize(16);
        self.font16U.setUnderline(True);

        self.font16BU.setFamily(FONT);
        self.font16BU.setPointSize(16);
        self.font16BU.setBold(True);
        self.font16BU.setUnderline(True);

        self.font18.setFamily(FONT);
        self.font18.setPointSize(18);

        self.font18B.setFamily(FONT);
        self.font18B.setPointSize(18);
        self.font18B.setBold(True);

        self.font18U.setFamily(FONT);
        self.font18U.setPointSize(18);
        self.font18U.setUnderline(True);

        self.font18BU.setFamily(FONT);
        self.font18BU.setPointSize(18);
        self.font18BU.setUnderline(True);
        self.font18BU.setBold(True);

        self.font20.setFamily(FONT);
        self.font20.setPointSizeF(20);

        self.font20B.setFamily(FONT);
        self.font20B.setPointSizeF(20);
        self.font20B.setBold(True);

        self.font20I.setFamily(FONT);
        self.font20I.setPointSizeF(20);
        self.font20I.setItalic(True);

        self.font20U.setFamily(FONT);
        self.font20U.setPointSizeF(20);
        self.font20U.setUnderline(True);

        self.font20UB.setFamily(FONT);
        self.font20UB.setPointSizeF(20);
        self.font20UB.setUnderline(True);
        self.font20UB.setBold(True);

        self.font24.setFamily(FONT);
        self.font24.setPointSize(24);

        self.font24B.setFamily(FONT);
        self.font24B.setPointSize(24);
        self.font24B.setBold(True);

        self.font24BU.setFamily(FONT);
        self.font24BU.setPointSize(24);
        self.font24BU.setUnderline(True);
        self.font24BU.setBold(True);

        self.font30B.setFamily(FONT);
        self.font30B.setPointSize(30);
        self.font30B.setBold(True);

        self.font30BU.setFamily(FONT);
        self.font30BU.setPointSize(30);
        self.font30BU.setBold(True);
        self.font30BU.setUnderline(True);

class ShoppingItem(QListWidgetItem):
    def __init__(self, list_widget, itemTitle, ID):
        super(ShoppingItem, self).__init__()
        self.itemTitle = itemTitle
        self.ID = ID
        self.item = QListWidgetItem()
        self.widget = QWidget()
        self.widget.setStyleSheet("background-color: white; border: transparent; border-radius: 0;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widgetItem = None
        self.list_widget = list_widget
        self.widgetLayout = QGridLayout(self.widget)
        # self.widgetLayout = QHBoxLayout(self.widget)
        
        font10B = QFont();
        font10B.setFamily(FONT);
        font10B.setPointSize(10);
        font10B.setBold(True);
        font12B = QFont();
        font12B.setFamily(FONT);
        font12B.setPointSize(12);
        font12B.setBold(True);
        widgetText = QLabel(self.widget)
        widgetText.setText(self.itemTitle)
        widgetText.setFont(font12B)
        widgetText.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        widgetText.setStyleSheet("background-color: transparent; color: #7e8198; padding: 0")
        self.crossMarkButton = QPushButton(self.widget)
        self.crossMarkButton.setText("Remove")
        self.crossMarkButton.setFont(font10B)
        self.crossMarkButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.crossMarkButton.setStyleSheet("""QPushButton{ background-color: #ff8f78; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                    QPushButton::pressed{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                    QPushButton::hover{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }""")
        self.crossMarkButton.clicked.connect(self.crossMarkButnClickedHandle)
        self.checkMarkButton = QPushButton(self.widget)
        self.checkMarkButton.setText("Done")
        self.checkMarkButton.setFont(font10B)
        self.checkMarkButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.checkMarkButton.setStyleSheet("""QPushButton{ background-color: #ff8f78; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                    QPushButton::pressed{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                    QPushButton::hover{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }""")
        self.checkMarkButton.clicked.connect(self.checkMarkButnClickedHandle)
        hSeparator = QWidget(self.widget)
        hSeparator.setFixedHeight(2)
        hSeparator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        hSeparator.setStyleSheet("background-color: #eaebec; padding-left: 10px; padding-right: 10px; padding-top: 10px")
        self.widgetLayout.addWidget(widgetText, 0, 0, 1, 1)
        self.widgetLayout.addItem(QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Maximum), 0, 1, 1, 1) # w:15 h:15
        self.widgetLayout.addWidget(self.crossMarkButton, 0, 2, 1, 1)
        self.widgetLayout.addWidget(self.checkMarkButton, 0, 3, 1, 1)
        self.widgetLayout.addWidget(hSeparator, 1, 0, 1, 4)
        self.widgetLayout.setColumnStretch(0, 0)
        self.widgetLayout.setColumnStretch(1, 1)
        self.widgetLayout.setColumnStretch(2, 0)
        self.widgetLayout.setColumnStretch(3, 0)
        self.widget.setLayout(self.widgetLayout)
        self.item.setSizeHint(self.widget.sizeHint())

    def crossMarkButnClickedHandle(self):
        self.remove()

    def checkMarkButnClickedHandle(self):
        self.remove()

    def insert(self, top=True):
        if top:
            self.list_widget.insertItem(0, self.item)
            self.widgetItem = self.list_widget.item(0)
        else:
            self.list_widget.addItem(self.item)
            self.widgetItem = self.list_widget.item(self.list_widget.count() - 1)
        self.list_widget.setItemWidget(self.item, self.widget)

    def remove(self):
        row = self.list_widget.row(self.widgetItem)
        self.list_widget.takeItem(row)

class TransactionItem(QListWidgetItem):
    def __init__(self, list_widget, ID, timeTranc, titleTranc, payment, type, cost):
        super(TransactionItem, self).__init__()
        self.ID = ID
        self.item = QListWidgetItem()
        self.widget = QWidget()
        self.widget.setStyleSheet("background-color: white; border: transparent; border-radius: 0;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.type = type[0].upper() + type[1:].lower()
        self.widget.setSizePolicy(sizePolicy)
        self.list_widget = list_widget
        self.widgetItem = None
        self.widgetLayout = QGridLayout(self.widget)
        colorTag = {"Other": "#51546f",
                    "Bills": "#7963cd",
                    "Entertaiment": "#ff8f78",
                    "Health": "#c13c3c",
                    "Education": "#3dbce0",
                    "Clothes": "#cbb64d",
                    "Salary": "#277a44"}
        # self.widgetLayout = QHBoxLayout(self.widget)

        font10B = QFont();
        font10B.setFamily(FONT);
        font10B.setPointSize(10);
        font10B.setBold(True);
        font12B = QFont();
        font12B.setFamily(FONT);
        font12B.setPointSize(12);
        font12B.setBold(True);
        font12N = QFont();
        font12N.setFamily(FONT);
        font12N.setPointSize(12);

        self.timeTrancLabel = QLabel(self.widget)
        self.timeTrancLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.timeTrancLabel.setStyleSheet("background-color: white; color: #1d1c1c; border: transparent; border-radius: 0;")
        self.timeTrancLabel.setFont(font12B)
        self.timeTrancLabel.setAlignment(Qt.AlignLeft)
        self.timeTrancLabel.setText(timeTranc)
        self.titleTrancLabel = QLabel(self.widget)
        self.titleTrancLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.titleTrancLabel.setStyleSheet("background-color: white; color: #1d1c1c; border: transparent; border-radius: 0;")
        self.titleTrancLabel.setFont(font12B)
        self.titleTrancLabel.setAlignment(Qt.AlignLeft)
        self.titleTrancLabel.setText(titleTranc)
        self.paymentMethodTrancLabel = QLabel(self.widget)
        self.paymentMethodTrancLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.paymentMethodTrancLabel.setStyleSheet("background-color: white; color: #7d7d7d; border: transparent; border-radius: 0;")
        self.paymentMethodTrancLabel.setFont(font12B)
        self.paymentMethodTrancLabel.setAlignment(Qt.AlignLeft)
        self.paymentMethodTrancLabel.setText(payment)
        tag = QWidget(self.widget)
        tag.setFixedSize(10, 10)
        tag.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.typeTrancLabel = QLabel(self.widget)
        self.typeTrancLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        try:
            self.typeTrancLabel.setStyleSheet("background-color: white; color: {}; border: transparent; border-radius: 0;".format(colorTag[self.type]))
            tag.setStyleSheet("background-color: {}; opacity: 0.5;".format(colorTag[self.type]))
        except KeyError:
            self.typeTrancLabel.setStyleSheet("background-color: white; color: #1d1c1c; border: transparent; border-radius: 0;")
            tag.setStyleSheet("background-color: #1d1c1c; opacity: 0.5;")

        self.typeTrancLabel.setFont(font12B)
        self.typeTrancLabel.setAlignment(Qt.AlignLeft)
        self.typeTrancLabel.setText(self.type)
        self.costTrancLabel = QLabel(self.widget)
        self.costTrancLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        if self.type == "Salary":
            self.costTrancLabel.setStyleSheet("background-color: white; color: #277a44; border: transparent; border-radius: 0;")
        else:
            self.costTrancLabel.setStyleSheet("background-color: white; color: #1d1c1c; border: transparent; border-radius: 0;")
        self.costTrancLabel.setFont(font12B)
        self.costTrancLabel.setAlignment(Qt.AlignRight)
        if self.type == "Salary":
            self.costTrancLabel.setText("+ " + currency(cost, brief=True) if cost>=1e6 else "+ " + currency(cost))
        else:
            self.costTrancLabel.setText("- " + currency(cost, brief=True) if cost>=1e6 else "- " + currency(cost))

        hSeparator = QWidget(self.widget)
        hSeparator.setFixedHeight(2)
        hSeparator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        hSeparator.setStyleSheet("background-color: #eaebec; padding-left: 10px; padding-right: 10px; padding-top: 10px")
        self.widgetLayout.addWidget(self.timeTrancLabel, 0, 0, 1, 1)
        self.widgetLayout.addWidget(self.titleTrancLabel, 0, 1, 1, 1)
        self.widgetLayout.addWidget(self.paymentMethodTrancLabel, 0, 2, 1, 1)
        self.widgetLayout.addWidget(tag, 0, 3, 1, 1)
        self.widgetLayout.addWidget(self.typeTrancLabel, 0, 4, 1, 1)
        self.widgetLayout.addWidget(self.costTrancLabel, 0, 5, 1, 1)
        self.widgetLayout.addWidget(hSeparator, 1, 0, 1, 6)
        self.widgetLayout.setColumnStretch(0, 5)
        self.widgetLayout.setColumnStretch(1, 40)
        self.widgetLayout.setColumnStretch(2, 10)
        self.widgetLayout.setColumnStretch(4, 10)
        self.widgetLayout.setColumnStretch(5, 10)
        self.widget.setLayout(self.widgetLayout)
        self.item.setSizeHint(self.widget.sizeHint())

    def crossMarkButnClickedHandle(self):
        self.remove()

    def checkMarkButnClickedHandle(self):
        self.remove()

    def insert(self, top=True):
        if top:
            self.list_widget.insertItem(0, self.item)
            self.widgetItem = self.list_widget.item(0)
        else:
            self.list_widget.addItem(self.item)
            self.widgetItem = self.list_widget.item(self.list_widget.count() - 1)
        self.list_widget.setItemWidget(self.item, self.widget)

    def remove(self):
        row = self.list_widget.row(self.widgetItem)
        self.list_widget.takeItem(row)

class AppWindow(QMainWindow):
    def __init__(self, app):
        super(AppWindow, self).__init__()
        screen = app.primaryScreen()
        rect = screen.availableGeometry()
        self.title = "Ứng dụng quản lý chi tiêu"
        self.l = 0
        if OS.startswith("win"):
            self.t = 0
        elif OS.startswith("linux"):
            self.t = 0
        elif OS.startswith("darwin"):
            self.t = 0
        else:
            sys.exit(1)
        self.w = rect.width()
        self.h = rect.height() - self.t
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint);
        self.initUI()
        self.closeEvent = self._closeEvent

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.l, self.t, self.w, self.h)
        self._font = MFont()
        self.widget = QWidget()
        # self.widget.setStyleSheet("background-color: #f2f3f7")
        self.windowLayout = QGridLayout(self.widget)
        self.windowLayout.addItem(QSpacerItem(20, 0, QSizePolicy.Maximum, QSizePolicy.Maximum), 0, 0, 1, 1) # w:20 h:10
        self.stackedWidget = QStackedWidget(self.widget)
        self.tabBarWidget = QWidget(self.widget)
        # self.tabBarWidget.setStyleSheet("border: 5px solid #4c4c4d;")
        self.initTabBar()
        self.windowLayout.addWidget(self.tabBarWidget, 1, 1, 1, 1)
        self.initStackedWidget()
        self.windowLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)
        self.windowLayout.addItem(QSpacerItem(20, 10, QSizePolicy.Maximum, QSizePolicy.Maximum), 3, 2, 1, 1) # w:20 h:10
        self.windowLayout.setColumnStretch(0, 0)
        self.windowLayout.setColumnStretch(1, 1)
        self.windowLayout.setColumnStretch(2, 0)
        self.windowLayout.setRowStretch(0, 0)
        self.windowLayout.setRowStretch(1, 1)
        self.windowLayout.setRowStretch(2, 10)
        self.windowLayout.setRowStretch(3, 0)
        self.widget.setLayout(self.windowLayout)
        self.setCentralWidget(self.widget)

    def initTabBar(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabBarWidget.sizePolicy().hasHeightForWidth())
        self.tabBarWidget.setSizePolicy(sizePolicy)
        self.tabBarWidgetLayout = QHBoxLayout(self.tabBarWidget)
        self.tabBarWidgetLayout.setSpacing(0)
        icon_app = QLabel(self.tabBarWidget)
        icon_app.setPixmap(QPixmap("image/logo_icon.png"))
        self.tabBarWidgetLayout.addWidget(icon_app)
        self.tabBarWidgetLayout.addItem(QSpacerItem(15, 10, QSizePolicy.Maximum, QSizePolicy.Maximum)) # w:15 h:10
        title_app = QLabel(self.tabBarWidget)
        title_app.setText("MyApp")
        title_app.setFont(self._font.font16B)
        title_app.setStyleSheet("color: #1d1c1c")
        self.tabBarWidgetLayout.addWidget(title_app)
        self.tabBarWidgetLayout.addItem(QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Maximum)) # w:40 h:10
        # self.separator = []
        # for i in range(5):
        #     separator = QFrame(self.tabBarWidget)
        #     separator.setFixedHeight(30)
        #     separator.setFrameShape(QFrame.VLine)
        #     separator.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        #     separator.setLineWidth(2)
        #     separator.setStyleSheet("color: #abacbc")
        #     self.separator.append(separator)

        # self.tabBarWidgetLayout.addWidget(self.separator[0])
        self.tabButtonList = []
        for i, label in enumerate(["My Account", "Transactions", "Cards", "Gold Forex Rate"]):
            tabButton = QPushButton(self.tabBarWidget)
            sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(tabButton.sizePolicy().hasHeightForWidth())
            tabButton.setSizePolicy(sizePolicy)
            tabButton.setSizePolicy(sizePolicy)
            tabButton.setStyleSheet(self.tabButtonStyleSheet(i, False))
            tabButton.clicked.connect(partial(self.onChangeTab, i))
            tabButton.setText(label)
            tabButton.setFont(self._font.font16B)
            self.tabBarWidgetLayout.addWidget(tabButton)
            # self.tabBarWidgetLayout.addWidget(self.separator[i + 1])
            self.tabButtonList.append(tabButton)

        self.tabBarWidgetLayout.addItem(QSpacerItem(15, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)) # Vertical Space
        settingButton = QPushButton(self.tabBarWidget)
        settingButton.setText("❀")
        settingButton.setFont(self._font.font24)
        settingButton.setStyleSheet("background-color: rgba(206, 217, 220, 0.0); color: #7a7c93; border: transparent; padding: 0; border-radius: 0;")
        self.tabBarWidgetLayout.addWidget(settingButton)
        self.usernameLabel = QLabel(self.tabBarWidget)
        self.usernameLabel.setText(username)
        self.usernameLabel.setFont(self._font.font16B)
        self.usernameLabel.setStyleSheet("color: #1d1c1c; padding: 10")
        self.tabBarWidgetLayout.addWidget(self.usernameLabel)
        self.avatarLabel = QLabel(self.tabBarWidget)
        self.avatarLabel.setFixedSize(70, 70)
        self.avatarLabel.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 15px; border: 5px solid #4c4c4d;")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avatarLabel.sizePolicy().hasHeightForWidth())
        self.avatarLabel.setSizePolicy(sizePolicy)
        self.avatarLabel.setSizePolicy(sizePolicy)
        self.avatarLabel.setPixmap(QPixmap(avatar).scaled(self.avatarLabel.width(), self.avatarLabel.height(), Qt.KeepAspectRatio, Qt.FastTransformation))
        self.tabBarWidgetLayout.addWidget(self.avatarLabel)
        self.tabBarWidgetLayout.setStretch(3, 1)
        self.tabBarWidgetLayout.setStretch(8, 7)
        self.tabBarWidget.setLayout(self.tabBarWidgetLayout)
        self.onChangeTab(0)

    def tabButtonStyleSheet(self, index, pressed):
        if pressed:
            styleSheet = """QPushButton{ background-color: rgba(206, 217, 220, 0.0); color: #242525; border: transparent; padding: 20; border-radius: 0; }"""
        else:
            styleSheet = """QPushButton{ background-color: rgba(206, 217, 220, 0.0); color: #7a7c93; border: transparent; padding: 10; border-radius: 0; }
                            QPushButton:hover{ background-color: rgba(206, 217, 220, 0.5); color: #7a7c93; border: transparent; padding: 10; border-radius: 0; }"""
        return styleSheet

    def onChangeTab(self, index):
        self._tab_selected = index
        self.stackedWidget.setCurrentIndex(self._tab_selected)
        for i in range(len(self.tabButtonList)):
            self.tabButtonList[i].setStyleSheet(self.tabButtonStyleSheet(i, False))
            self.tabButtonList[i].setFont(self._font.font14B)
            self.tabButtonList[i].setEnabled(True)

        # for i in range(len(self.separator)):
        #     self.separator[i].setStyleSheet("color: #abacbc")
        #     self.separator[i].setFixedHeight(30)
        #     self.separator[i].setLineWidth(2)

        self.tabButtonList[self._tab_selected].setStyleSheet(self.tabButtonStyleSheet(self._tab_selected, True))
        self.tabButtonList[self._tab_selected].setEnabled(False)
        self.tabButtonList[self._tab_selected].setFont(self._font.font16BU)
        # self.separator[self._tab_selected].setStyleSheet("color: #242525")
        # self.separator[self._tab_selected].setFixedHeight(35)
        # self.separator[self._tab_selected].setLineWidth(3)
        # self.separator[self._tab_selected + 1].setStyleSheet("color: #242525")
        # self.separator[self._tab_selected + 1].setFixedHeight(40)
        # self.separator[self._tab_selected + 1].setLineWidth(3)

    def initStackedWidget(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.addWidget(self.initMyAccountTab())
        self.stackedWidget.addWidget(self.initTransactionsTab())
        self.stackedWidget.addWidget(self.initCardsTab())
        self.stackedWidget.addWidget(self.initGoldForexRateTab())

    def initMyAccountTab(self):
        tabWidget = QWidget(self.stackedWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tabWidget.sizePolicy().hasHeightForWidth())
        tabWidget.setSizePolicy(sizePolicy)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tabWidget.sizePolicy().hasHeightForWidth())
        tabWidget.setSizePolicy(sizePolicy)
        tabWidgetLayout = QVBoxLayout(tabWidget)
        tabWidgetRow0 = QWidget(tabWidget)
        tabWidgetRow0Layout = QHBoxLayout(tabWidgetRow0)
        tabWidgetRow1 = QWidget(tabWidget)
        tabWidgetRow1Layout = QHBoxLayout(tabWidgetRow1)
        tabWidgetLayout.addWidget(tabWidgetRow0)
        tabWidgetLayout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum)) # w:15 h:15
        tabWidgetLayout.addWidget(tabWidgetRow1)
        tabWidgetLayout.setSpacing(0)

        def initAccountWidget(accountWidget):
            accountWidget.setStyleSheet("border: transparent; background-color: white; border-radius: 15px;")
            # accountWidget.setStyleSheet("border: transparent; background-color: transparent; border-radius: 15px;")
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(accountWidget.sizePolicy().hasHeightForWidth())
            accountWidget.setSizePolicy(sizePolicy)
            accountWidgetLayout = QHBoxLayout(accountWidget)
            accountWidgetLayout.setSpacing(5)

            accountWidgetColumn0 = QWidget(accountWidget)
            accountWidgetColumn0Layout = QVBoxLayout(accountWidgetColumn0)
            selectAccoutWidget = QWidget(accountWidgetColumn0)
            selectAccoutWidgetLayout = QHBoxLayout(selectAccoutWidget)
            self.prevAccButton = QPushButton(selectAccoutWidget)
            self.prevAccButton.setText("◄")
            self.prevAccButton.setFont(self._font.font14)
            self.prevAccButton.setStyleSheet("""QPushButton{ background-color: #daf2ef; color: #51546f; border: transparent; padding: 10; border-radius: 10; }
                                                QPushButton::pressed{ background-color: #767891; color: #3c3e54; border: transparent; padding: 10; border-radius: 10; }
                                                QPushButton::hover{ background-color: #e1f5f2; color: #7a7c93; border: transparent; padding: 10; border-radius: 10; }""")
            sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.prevAccButton.sizePolicy().hasHeightForWidth())
            self.prevAccButton.setSizePolicy(sizePolicy)
            self.nameAccountLabel = QLabel(selectAccoutWidget)
            self.nameAccountLabel.setText("Main Account")
            self.nameAccountLabel.setFont(self._font.font14B)
            self.nameAccountLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.nameAccountLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.nameAccountLabel.sizePolicy().hasHeightForWidth())
            self.nameAccountLabel.setSizePolicy(sizePolicy)
            self.nextAccButton = QPushButton(selectAccoutWidget)
            self.nextAccButton.setText("►")
            self.nextAccButton.setFont(self._font.font14)
            self.nextAccButton.setStyleSheet("""QPushButton{ background-color: #daf2ef; color: #51546f; border: transparent; padding: 10; border-radius: 10; }
                                                QPushButton::pressed{ background-color: #767891; color: #3c3e54; border: transparent; padding: 10; border-radius: 10; }
                                                QPushButton::hover{ background-color: #e1f5f2; color: #7a7c93; border: transparent; padding: 10; border-radius: 10; }""")
            sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.nextAccButton.sizePolicy().hasHeightForWidth())
            selectAccoutWidgetLayout.addWidget(self.prevAccButton)
            selectAccoutWidgetLayout.addWidget(self.nameAccountLabel)
            selectAccoutWidgetLayout.addWidget(self.nextAccButton)
            selectAccoutWidgetLayout.addItem(QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:15 h:15
            selectAccoutWidgetLayout.setStretch(1, 3)
            selectAccoutWidgetLayout.setStretch(3, 2)
            selectAccoutWidget.setLayout(selectAccoutWidgetLayout)

            self.accountTitleLabel = QLabel(accountWidgetColumn0)
            self.accountTitleLabel.setText("Minh Nguyen Thi")
            self.accountTitleLabel.setFont(self._font.font20B)
            self.accountTitleLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding: 10;")
            
            self.accountbriefLabel = QLabel(accountWidgetColumn0)
            self.accountbriefLabel.setText("from Sep, 19th 2020 to Oct, 22nd 2020")
            self.accountbriefLabel.setFont(self._font.font12B)
            self.accountbriefLabel.setAlignment(Qt.AlignTop)
            self.accountbriefLabel.setStyleSheet("background-color: transparent; color: #757890; border: transparent; padding: 10;")

            navigatorWidget = QWidget(accountWidgetColumn0)
            navigatorWidgetLayout = QHBoxLayout(navigatorWidget)
            self.gotoDetailTabButn = QPushButton(navigatorWidget)
            self.gotoDetailTabButn.setFont(self._font.font14B)
            self.gotoDetailTabButn.setText("Details")
            self.gotoDetailTabButn.setStyleSheet("""QPushButton{ background-image: url(image/button-icon-enabled.png); background-position: center; background-color: #058373; color: #d5e9e7; border: transparent; padding: 20; border-radius: 20; }
                                                    QPushButton::disabled{ background-image: url(image/button-icon-disabled.png); background-color: #f2f3f8; color: #a7a9b5; border: transparent; padding: 20; border-radius: 20; }
                                                    QPushButton::hover{ background-color: #10a391; color: #d3e3e1; border: transparent; padding: 20; border-radius: 20; }""")
            self.gotoCardTabButn = QPushButton(navigatorWidget)
            self.gotoCardTabButn.setFont(self._font.font14B)
            self.gotoCardTabButn.setText("Card Information")
            self.gotoCardTabButn.setStyleSheet("""QPushButton{ background-image: url(image/button-icon-enabled.png); background-color: #058373; color: #d5e9e7; border: transparent; padding: 20; border-radius: 20; }
                                                    QPushButton::disabled{ background-image: url(image/button-icon-disabled.png); background-color: #f2f3f8; color: #a7a9b5; border: transparent; padding: 20; border-radius: 20; }
                                                    QPushButton::hover{ background-color: #10a391; color: #d3e3e1; border: transparent; padding: 20; border-radius: 20; }""")
            self.gotoCardTabButn.setEnabled(False)
            navigatorWidgetLayout.addWidget(self.gotoDetailTabButn)
            navigatorWidgetLayout.addWidget(self.gotoCardTabButn)
            navigatorWidgetLayout.addItem(QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Maximum)) # w:15 h:15
            navigatorWidgetLayout.setStretch(0, 2)
            navigatorWidgetLayout.setStretch(1, 2)
            navigatorWidgetLayout.setStretch(2, 1)
            navigatorWidget.setLayout(navigatorWidgetLayout)

            accountWidgetColumn0Layout.addWidget(selectAccoutWidget)
            accountWidgetColumn0Layout.addWidget(self.accountTitleLabel)
            accountWidgetColumn0Layout.addWidget(self.accountbriefLabel)
            accountWidgetColumn0Layout.addWidget(navigatorWidget)
            accountWidgetColumn0Layout.setStretch(0, 0)
            accountWidgetColumn0Layout.setStretch(1, 2)
            accountWidgetColumn0Layout.setStretch(2, 2)
            accountWidgetColumn0Layout.setStretch(3, 2)
            accountWidgetColumn0.setLayout(accountWidgetColumn0Layout)

            accountWidgetColumn1 = QWidget(accountWidget)
            accountWidgetColumn1Layout = QGridLayout(accountWidgetColumn1)
            accountWidgetColumn1Layout.setSpacing(0)
            availBalanceTextLabel = QLabel(accountWidgetColumn1)
            availBalanceTextLabel.setText("Available balance")
            availBalanceTextLabel.setFont(self._font.font12B)
            availBalanceTextLabel.setAlignment(Qt.AlignRight)
            availBalanceTextLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")
            
            colorTagAvailBalance = QFrame(accountWidgetColumn1)
            colorTagAvailBalance.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
            colorTagAvailBalance.setFixedWidth(10)
            colorTagAvailBalance.setStyleSheet("background-color: #41ab2e; color: #41ab2e")

            self.availBalanceLabel = QLabel(accountWidgetColumn1)
            self.availBalanceLabel.setText(currency(31076464))
            self.availBalanceLabel.setFont(self._font.font30BU)
            self.availBalanceLabel.setAlignment(Qt.AlignRight)
            self.availBalanceLabel.setStyleSheet("background-color: transparent; color: #2f5240; border: transparent; padding: 10;")
            
            expenseTextLabel = QLabel(accountWidgetColumn1)
            expenseTextLabel.setText("Expenses")
            expenseTextLabel.setFont(self._font.font12B)
            expenseTextLabel.setAlignment(Qt.AlignRight | Qt.AlignBottom)
            expenseTextLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")

            self.expenseLabel = QLabel(accountWidgetColumn1)
            self.expenseLabel.setText(currency(2200000, brief=True))
            self.expenseLabel.setFont(self._font.font24B)
            self.expenseLabel.setAlignment(Qt.AlignRight)
            self.expenseLabel.setStyleSheet("background-color: transparent; color: #102a3b; border: transparent; padding: 10;")

            colorTagExpenses = QFrame(accountWidgetColumn1)
            colorTagExpenses.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            colorTagExpenses.setFixedHeight(expenseTextLabel.height()*2 + self.expenseLabel.height())
            colorTagExpenses.setFixedWidth(10)
            colorTagExpenses.setStyleSheet("background-color: #4791bf; color: #4791bf")

            incomeTextLabel = QLabel(accountWidgetColumn1)
            incomeTextLabel.setText("Income")
            incomeTextLabel.setFont(self._font.font12B)
            incomeTextLabel.setAlignment(Qt.AlignRight | Qt.AlignBottom)
            incomeTextLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")

            self.incomeLabel = QLabel(accountWidgetColumn1)
            self.incomeLabel.setText(currency(10000000, brief=True))
            self.incomeLabel.setFont(self._font.font24B)
            self.incomeLabel.setAlignment(Qt.AlignRight)
            self.incomeLabel.setStyleSheet("background-color: transparent; color: #4d340b; border: transparent; padding: 10;")

            colorTagIncome = QFrame(accountWidgetColumn1)
            colorTagIncome.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            colorTagIncome.setFixedHeight(incomeTextLabel.height()*2 + self.incomeLabel.height())
            colorTagIncome.setFixedWidth(10)
            colorTagIncome.setStyleSheet("background-color: #e39517; color: #e39517")

            accountWidgetColumn1Layout.addWidget(availBalanceTextLabel, 0, 0, 1, 4)
            accountWidgetColumn1Layout.addWidget(self.availBalanceLabel, 1, 0, 1, 4)
            accountWidgetColumn1Layout.addWidget(colorTagAvailBalance, 0, 4, 2, 1)
            accountWidgetColumn1Layout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum))
            accountWidgetColumn1Layout.addWidget(expenseTextLabel, 3, 0, 1, 1)
            accountWidgetColumn1Layout.addWidget(self.expenseLabel, 4, 0, 1, 1)
            accountWidgetColumn1Layout.addWidget(colorTagExpenses, 3, 1, 2, 1)
            accountWidgetColumn1Layout.addWidget(incomeTextLabel, 3, 3, 1, 1)
            accountWidgetColumn1Layout.addWidget(self.incomeLabel, 4, 3, 1, 1)
            accountWidgetColumn1Layout.addWidget(colorTagIncome, 3, 4, 2, 1)
            accountWidgetColumn1.setLayout(accountWidgetColumn1Layout)

            accountWidgetLayout.addWidget(accountWidgetColumn0)
            accountWidgetLayout.addWidget(accountWidgetColumn1)
            accountWidgetLayout.setStretch(0, 1)
            accountWidgetLayout.setStretch(1, 1)
            accountWidget.setLayout(accountWidgetLayout)

        accountWidget = QWidget(tabWidget)
        initAccountWidget(accountWidget)
        
        def initShopTodayWidget(shopTodayWidget):
            shopTodayWidget.setStyleSheet("border: transparent; background-color: #058272; border-radius: 15px;")
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(shopTodayWidget.sizePolicy().hasHeightForWidth())
            shopTodayWidget.setSizePolicy(sizePolicy)
            shopTodayWidgetLayout = QGridLayout(shopTodayWidget)
            shopTodayWidgetLayout.setSpacing(5)
            shopTodayTitleLabel = QLabel(shopTodayWidget)
            shopTodayTitleLabel.setText("Shopping List")
            shopTodayTitleLabel.setFont(self._font.font16B)
            shopTodayTitleLabel.setAlignment(Qt.AlignLeft)
            shopTodayTitleLabel.setStyleSheet("background-color: transparent; color: #dbedeb; border: transparent; padding: 10;")
            shopTodayTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

            # checkButton = QPushButton(shopTodayWidget)
            # checkButton.setText("Done")
            # checkButton.setFont(self._font.font14B)
            # checkButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            # checkButton.setMaximumWidth(70)
            # checkButton.setStyleSheet("""QPushButton{ background-color: #ff8f78; color: #ffffff; border: transparent; padding: 3; border-radius: 10; }
            #                             QPushButton::pressed{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 3; border-radius: 10; }
            #                             QPushButton::hover{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 3; border-radius: 10; }""")
            plusButton = QPushButton(shopTodayWidget)
            plusButton.setText(" Add ")
            plusButton.setFont(self._font.font14B)
            plusButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            plusButton.setMaximumWidth(70)
            plusButton.setStyleSheet("""QPushButton{ background-color: #ff8f78; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                        QPushButton::pressed{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                        QPushButton::hover{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }""")
            # minusButton = QPushButton(shopTodayWidget)
            # minusButton.setText("  −  ")
            # minusButton.setFont(self._font.font14B)
            # minusButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            # minusButton.setMaximumWidth(70)
            # minusButton.setStyleSheet("""QPushButton{ background-color: #ff8f78; color: #ffffff; border: transparent; padding: 3; border-radius: 10; }
            #                             QPushButton::pressed{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 3; border-radius: 10; }
            #                             QPushButton::hover{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 3; border-radius: 10; }""")

            calendarIcon = QLabel(shopTodayWidget)
            calendarIcon.setFixedSize(30, 42)
            calendarIcon.setStyleSheet("background-color: transparent; border: transparent;")
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.avatarLabel.sizePolicy().hasHeightForWidth())
            calendarIcon.setSizePolicy(sizePolicy)
            calendarIcon.setPixmap(QPixmap("image/favpng_e-commerce-online-shopping-icon.png").scaled(calendarIcon.width(), calendarIcon.height(), Qt.KeepAspectRatio, Qt.FastTransformation))

            self.shoppingListWidget = QListWidget(shopTodayWidget)
            self.shoppingListItems = []
            for _title in ["bought some of OMAI", "Buy new Iphone 12 Pro Max", "Buy a Package of condom", "Buy new laptop", "Buy new Samsung Galaxy S21 Ultra", "Buy new sugar baby"]:
                item = ShoppingItem(self.shoppingListWidget, _title, uuid4().hex)
                item.insert()
                self.shoppingListItems.append(item)

            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.shoppingListWidget.sizePolicy().hasHeightForWidth())
            self.shoppingListWidget.setSizePolicy(sizePolicy)
            self.shoppingListWidget.setStyleSheet("background-color: transparent; color: #dbedeb; border: transparent; padding: 10;")

            paddingWidget = QWidget(shopTodayWidget)
            paddingWidgetLayout = QHBoxLayout(paddingWidget)
            paddingWidgetLayout.setSpacing(10)
            paddingWidgetLayout.addWidget(self.shoppingListWidget)
            paddingWidget.setLayout(paddingWidgetLayout)

            shopTodayWidgetLayout.addWidget(shopTodayTitleLabel, 0, 0, 1, 1)
            # shopTodayWidgetLayout.addWidget(minusButton, 0, 2, 1, 1)
            shopTodayWidgetLayout.addWidget(plusButton, 0, 1, 1, 1)
            # shopTodayWidgetLayout.addWidget(checkButton, 0, 4, 1, 1)
            # shopTodayWidgetLayout.addItem(QSpacerItem(5, 5, QSizePolicy.Maximum, QSizePolicy.Maximum), 3, 0, 1, 1) # w:15 h:15
            shopTodayWidgetLayout.addWidget(calendarIcon, 0, 2, 1, 1)
            shopTodayWidgetLayout.addWidget(paddingWidget, 1, 0, 1, 3)
            shopTodayWidgetLayout.setColumnStretch(0, 10)
            # shopTodayWidgetLayout.setColumnStretch(2, 3)
            # shopTodayWidgetLayout.setColumnStretch(, 3)
            # shopTodayWidgetLayout.setColumnStretch(4, 3)
            # shopTodayWidgetLayout.setColumnStretch(3, 0)
            # shopTodayWidgetLayout.setColumnStretch(3, 0)
            shopTodayWidget.setLayout(shopTodayWidgetLayout)

        shopTodayWidget = QWidget(tabWidget)
        initShopTodayWidget(shopTodayWidget)

        def initLatestTrancWidget(latestTrancWidget):
            latestTrancWidget.setStyleSheet("border: transparent; background-color: white; border-radius: 15px;")
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(latestTrancWidget.sizePolicy().hasHeightForWidth())
            latestTrancWidget.setSizePolicy(sizePolicy)
            latestTrancWidgetLayout = QGridLayout(latestTrancWidget)
            latestTrancWidgetLayout.setSpacing(0)

            latestTrancWidget_row0 = QWidget(latestTrancWidget)
            latestTrancWidget_row0Layout = QHBoxLayout(latestTrancWidget_row0)
            latestTrancTitleLabel = QLabel(latestTrancWidget_row0)
            latestTrancTitleLabel.setText("Latest transactions")
            latestTrancTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            latestTrancTitleLabel.setFont(self._font.font16B)
            latestTrancTitleLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10;")
            self.moreDetailTabButn2 = QPushButton(latestTrancWidget_row0)
            self.moreDetailTabButn2.setText("➔")
            self.moreDetailTabButn2.setFont(self._font.font14B)
            self.moreDetailTabButn2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            self.moreDetailTabButn2.setStyleSheet("""QPushButton{ background-color: #058373; color: #cfe7e4; border: transparent; padding: 10; border-radius: 10; }
                                                    QPushButton:hover{ background-color: #0eab97; color: #c3e3df; border: transparent; padding: 10; border-radius: 10; }""")
            latestTrancWidget_row0Layout.addWidget(latestTrancTitleLabel)
            latestTrancWidget_row0Layout.addWidget(self.moreDetailTabButn2)
            latestTrancWidget_row0.setLayout(latestTrancWidget_row0Layout)

            hSeparator = QWidget(latestTrancWidget)
            hSeparator.setFixedHeight(2)
            hSeparator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            hSeparator.setStyleSheet("background-color: #eaebec; padding-left: 10px; padding-right: 10px")
            padding = QWidget(latestTrancWidget)
            paddingLayout = QHBoxLayout(padding)
            padding.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            padding.setStyleSheet("background-color: transparent")
            paddingLayout.addWidget(hSeparator)
            padding.setLayout(paddingLayout)
            padding2 = QWidget(latestTrancWidget)
            padding2Layout = QHBoxLayout(padding2)
            padding2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            padding2.setStyleSheet("background-color: transparent")
            padding2Layout.addWidget(padding)
            padding2.setLayout(padding2Layout)

            latestTrancWidget_row1 = QWidget(latestTrancWidget)
            latestTrancWidget_row1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            latestTrancWidget_row1Layout = QHBoxLayout(latestTrancWidget_row1)
            latestTrancWidget_row1.setLayout(latestTrancWidget_row1Layout)
            self.trancListWidget = QListWidget(latestTrancWidget)
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.trancListWidget.sizePolicy().hasHeightForWidth())
            self.trancListWidget.setSizePolicy(sizePolicy)
            self.trancListWidget.setStyleSheet("background-color: transparent; color: #dbedeb; border: transparent; border-radius: 0px;")
            self.trancListItems = []
            for _timeTranc, _titleTranc, _payment, _type, _cost in zip(["Today", "Today", "20.05", "20.05", "19.05", "19.05", "18.05",
                                                                            "17.05", "17.05", "16.05", "16.05", "15.05", "14.05"],
                                                                        ["Starbucks Cafe", "Off White Oxford Street 41", "Spotify Premium", "Viettel Network", "Allgero.pl Sp.z.o.o", "Super-Pharm Warsaw", "Carrefour Express",
                                                                            "HighLand coffee", "Vegetable", "Miss Quy's Birthday", "Dinner", "Gift for Miss Quy", "Bring my W to ice cream store"],
                                                                        ["Card payment", "Card payment", "Fee", "Transfer", "Blik", "Blik", "Card payment",
                                                                            "Card payment", "Cash", "Card payment", "Card payment", "Card payment", "Card payment"],
                                                                        ["Food", "Clothes", "Entertainment", "Salary", "Clothes", "Health", "Food",
                                                                            "Other", "Other", "Other", "Other", "Other", "Other"],
                                                                        [49000, 260000, 59000, 14000000, 25000, 98900, 45780,
                                                                            49000, 15000, 100000, 100000, 53000, 18000]):
                item = TransactionItem(self.trancListWidget, uuid4().hex, _timeTranc, _titleTranc, _payment, _type, _cost)
                item.insert(top=False)
                self.trancListItems.append(item)

            latestTrancWidget_row1Layout.addWidget(self.trancListWidget)
            latestTrancWidget_row1.setLayout(latestTrancWidget_row1Layout)

            latestTrancWidgetLayout.addWidget(latestTrancWidget_row0)
            latestTrancWidgetLayout.addWidget(padding2)
            latestTrancWidgetLayout.addWidget(latestTrancWidget_row1)
            latestTrancWidget.setLayout(latestTrancWidgetLayout)

        latestTrancWidget = QWidget(tabWidget)
        initLatestTrancWidget(latestTrancWidget)

        def initAllExpensesWidget(allExpensesWidget):
            allExpensesWidget.setStyleSheet("border: transparent; background-color: white; border-radius: 15px;")
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(allExpensesWidget.sizePolicy().hasHeightForWidth())
            allExpensesWidget.setSizePolicy(sizePolicy)
            allExpensesWidgetLayout = QVBoxLayout(allExpensesWidget)

            allExpensesWidget_row0 = QWidget(allExpensesWidget)
            allExpensesWidget_row0Layout = QHBoxLayout(allExpensesWidget_row0)
            allExpensesTitleLabel = QLabel(allExpensesWidget_row0)
            allExpensesTitleLabel.setText("All expenses")
            allExpensesTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            allExpensesTitleLabel.setFont(self._font.font16B)
            allExpensesTitleLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10;")
            self.gotoDetailTabButn2 = QPushButton(allExpensesWidget_row0)
            self.gotoDetailTabButn2.setText("➔")
            self.gotoDetailTabButn2.setFont(self._font.font14B)
            self.gotoDetailTabButn2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            self.gotoDetailTabButn2.setStyleSheet("""QPushButton{ background-color: #058373; color: #cfe7e4; border: transparent; padding: 10; border-radius: 10; }
                                                        QPushButton:hover{ background-color: #0eab97; color: #c3e3df; border: transparent; padding: 10; border-radius: 10; }""")
            allExpensesWidget_row0Layout.addWidget(allExpensesTitleLabel)
            allExpensesWidget_row0Layout.addWidget(self.gotoDetailTabButn2)
            allExpensesWidget_row0.setLayout(allExpensesWidget_row0Layout)

            allExpensesWidget_row1 = QWidget(allExpensesWidget)
            allExpensesWidget_row1Layout = QGridLayout(allExpensesWidget_row1)
            dailyTitleLabel = QLabel(allExpensesWidget_row1)
            dailyTitleLabel.setText("daily")
            dailyTitleLabel.setAlignment(Qt.AlignLeft)
            dailyTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            dailyTitleLabel.setFont(self._font.font12B)
            dailyTitleLabel.setStyleSheet("background-color: transparent; color: #72758e; border: transparent; padding-left: 10; padding-bottom: 0;")
            weeklyTitleLabel = QLabel(allExpensesWidget_row1)
            weeklyTitleLabel.setText("weekly")
            weeklyTitleLabel.setAlignment(Qt.AlignLeft)
            weeklyTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            weeklyTitleLabel.setFont(self._font.font12B)
            weeklyTitleLabel.setStyleSheet("background-color: transparent; color: #72758e; border: transparent; padding-left: 10; padding-bottom: 0;")
            monthlyTitleLabel = QLabel(allExpensesWidget_row1)
            monthlyTitleLabel.setText("monthly")
            monthlyTitleLabel.setAlignment(Qt.AlignLeft)
            monthlyTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            monthlyTitleLabel.setFont(self._font.font12B)
            monthlyTitleLabel.setStyleSheet("background-color: transparent; color: #72758e; border: transparent; padding-left: 10; padding-bottom: 0;")
            dailyLabel = QLabel(allExpensesWidget_row1)
            dailyLabel.setText(currency(275400, brief=True))
            dailyLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            dailyLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            dailyLabel.setFont(self._font.font18B)
            dailyLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10; padding-bottom: 0;")
            weeklyLabel = QLabel(allExpensesWidget_row1)
            weeklyLabel.setText(currency(1426000, brief=True))
            weeklyLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            weeklyLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            weeklyLabel.setFont(self._font.font18B)
            weeklyLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10; padding-bottom: 0;")
            monthlyLabel = QLabel(allExpensesWidget_row1)
            monthlyLabel.setText(currency(8200000, brief=True))
            monthlyLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            monthlyLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            monthlyLabel.setFont(self._font.font18B)
            monthlyLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10; padding-bottom: 0;")
            allExpensesWidget_row1Layout.addWidget(dailyTitleLabel, 0, 0, 1, 1)
            allExpensesWidget_row1Layout.addWidget(weeklyTitleLabel, 0, 1, 1, 1)
            allExpensesWidget_row1Layout.addWidget(monthlyTitleLabel, 0, 2, 1, 1)
            allExpensesWidget_row1Layout.addWidget(dailyLabel, 1, 0, 1, 1)
            allExpensesWidget_row1Layout.addWidget(weeklyLabel, 1, 1, 1, 1)
            allExpensesWidget_row1Layout.addWidget(monthlyLabel, 1, 2, 1, 1)
            allExpensesWidget_row1.setLayout(allExpensesWidget_row1Layout)

            allExpensesWidget_row2 = QWidget(allExpensesWidget)
            allExpensesWidget_row2Layout = QVBoxLayout(allExpensesWidget_row2)
            durationComboBox = QComboBox(allExpensesWidget_row2)
            durationComboBox.setFont(self._font.font12B)
            durationComboBox.setStyleSheet("""QComboBox{ background-color: transparent; padding-left: 15px }
                                                QComboBox:QAbstractItemView{ background-color: white; color:orange; padding-left: 15px }""")
            durationComboBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            durationComboBox.addItem("Today")
            durationComboBox.addItem("Yesterday")
            durationComboBox.addItem("2-day ago")
            durationComboBox.addItem("a week ago")
            durationComboBox.addItem("two-week ago")
            durationComboBox.addItem("a month ago")
            durationComboBox.addItem("custom")

            series = QPieSeries()
            series.setHoleSize(0.6)
            data = (820000, 820000, 752000, 522000, 300000, 450000)
            _sum = sum(data)
            dataLabel = ("Other", "Bills", "Entertaiment", "Health", "Education", "Clothes")
            colorLabel = ("#51546f", "#7963cd", "#ff8f78", "#c13c3c", "#3dbce0", "#cbb64d")
            for _data, _label, _color in zip(data, dataLabel, colorLabel):
                series.append(_label, _data)
                slice = QPieSlice()
                slice = series.slices()[series.count() - 1]
                # slice.setExploded(True)
                slice.setLabel("{}: {}".format(_label, currency(_data, "", brief=True)))
                slice.setLabelFont(self._font.font10BI)
                slice.setLabelVisible(True)
                slice.setPen(QPen(QColor(_color), 0))
                slice.setBrush(QColor(_color))

            chart = QChart()
            # chart.legend().hide()
            chart.addSeries(series)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chartview = QChartView(chart)
            chartview.setRenderHint(QPainter.Antialiasing)
            chart.legend().setAlignment(Qt.AlignRight)
            for i, _label in enumerate(dataLabel):
                chart.legend().markers(series)[i].setLabel(_label)
                chart.legend().markers(series)[i].setFont(self._font.font10B)
            allExpensesWidget_row2Layout.addWidget(durationComboBox)
            allExpensesWidget_row2Layout.addWidget(chartview)
            allExpensesWidget_row2.setLayout(allExpensesWidget_row2Layout)

            hSeparator = QWidget(allExpensesWidget)
            hSeparator.setFixedHeight(2)
            hSeparator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            hSeparator.setStyleSheet("background-color: #eaebec; padding-left: 10px; padding-left: 10px")
            padding = QWidget(allExpensesWidget)
            paddingLayout = QHBoxLayout(padding)
            padding.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            padding.setStyleSheet("background-color: transparent")
            paddingLayout.addWidget(hSeparator)
            padding.setLayout(paddingLayout)
            padding2 = QWidget(allExpensesWidget)
            padding2Layout = QHBoxLayout(padding2)
            padding2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
            padding2.setStyleSheet("background-color: transparent")
            padding2Layout.addWidget(padding)
            padding2.setLayout(padding2Layout)

            allExpensesWidgetLayout.addWidget(allExpensesWidget_row0)
            allExpensesWidgetLayout.addWidget(allExpensesWidget_row1)
            allExpensesWidgetLayout.addWidget(padding2)
            allExpensesWidgetLayout.addWidget(allExpensesWidget_row2)
            allExpensesWidgetLayout.setStretch(0, 1)
            allExpensesWidgetLayout.setStretch(1, 1)
            allExpensesWidgetLayout.setStretch(3, 5)
            allExpensesWidget.setLayout(allExpensesWidgetLayout)

        allExpensesWidget = QWidget(tabWidget)
        initAllExpensesWidget(allExpensesWidget)

        tabWidgetRow0Layout.addWidget(accountWidget)
        tabWidgetRow0Layout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum)) # w:15 h:15
        tabWidgetRow0Layout.addWidget(shopTodayWidget)
        tabWidgetRow0Layout.setStretch(0, 30)
        tabWidgetRow0Layout.setStretch(1, 1)
        tabWidgetRow0Layout.setStretch(2, 20)
        tabWidgetRow0.setLayout(tabWidgetRow0Layout)

        tabWidgetRow1Layout.addWidget(latestTrancWidget)
        tabWidgetRow1Layout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum)) # w:15 h:15
        tabWidgetRow1Layout.addWidget(allExpensesWidget)
        tabWidgetRow1Layout.setStretch(0, 30)
        tabWidgetRow1Layout.setStretch(1, 1)
        tabWidgetRow1Layout.setStretch(2, 20)
        tabWidgetRow1.setLayout(tabWidgetRow1Layout)

        tabWidgetLayout.setStretch(0, 2)
        tabWidgetLayout.setStretch(1, 0)
        tabWidgetLayout.setStretch(2, 4)
        tabWidget.setLayout(tabWidgetLayout)
        return tabWidget

    def initTransactionsTab(self):
        tabWidget = QWidget(self.stackedWidget)
        return tabWidget

    def initCardsTab(self):
        tabWidget = QWidget(self.stackedWidget)
        return tabWidget

    def initGoldForexRateTab(self):
        tabWidget = QWidget(self.stackedWidget)
        return tabWidget

    def _closeEvent(self, event):
        print("__close AppWindow__")

if __name__ == "__main__":
    stylesheet = """
        AppWindow {
            background-image: url(image/contour-dark-blue-lines-white.jpg);
            background-repeat: no-repeat;
            background-position: center;
        }
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = AppWindow(app)
    window.showFullScreen()
    sys.exit(app.exec_())



