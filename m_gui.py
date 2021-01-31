import sys
import os
from functools import partial
from PyQt5.QtCore import Qt, QRect, QTimer, QThread, QThreadPool, QRunnable, QObject, pyqtSignal, pyqtSlot, QSize
from PyQt5.QtWidgets import QComboBox, QMainWindow, QVBoxLayout, QHBoxLayout, QMessageBox, QProgressBar
from PyQt5.QtWidgets import QLabel, QFileDialog, QLineEdit, QFrame, QMenu, QInputDialog, QSpacerItem
from PyQt5.QtWidgets import QApplication, QAction, qApp, QGroupBox, QRadioButton, QSizePolicy, QFrame
from PyQt5.QtWidgets import QTabWidget, QWidget, QPushButton, QListWidget, QGridLayout, QStackedWidget
from PyQt5.QtWidgets import QDialog, QListWidgetItem, QScrollBar, QStyle
from PyQt5.QtGui import QColor, QFont, QPixmap, QIcon, QImage, QPainter, QPen
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLineSeries, QBarSet, QPercentBarSeries, QBarCategoryAxis
from uuid import uuid4
from datetime import datetime, date, time, timedelta

OS = sys.platform
username = "Minh Nguyen"
avatar = "image/avatar.png"
PAYMENT_METHOD = ["Other Method", "VN Pay", "Card Payment", "Fee", "Cash", "Momo", "Airpay", "Zalo Pay", "Transfer", "Grab by Moca"]
INCOME_TAG = {"Salary": "#277a44", "Other Income": "#72d6c2"}
EXPENSE_TAG = {"Other": "#51546f", "Food": "#b1d672", "Bills": "#7963cd", "Entertainment": "#ff8f78", "Health": "#c13c3c", "Education": "#3dbce0", "Clothes": "#cbb64d"}
TRANCS_TAG = dict(item for _dict in [EXPENSE_TAG, INCOME_TAG] for item in _dict.items())
MONTH = {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"}

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

class ShoppingItemSignals(QObject):
    signal_remove = pyqtSignal(int)
    signal_add = pyqtSignal(dict)

class ShoppingItem(QListWidgetItem):
    # signal = pyqtSignal(int)
    def __init__(self, list_widget, itemTitle, ID):
        super(ShoppingItem, self).__init__()
        self.itemTitle = itemTitle
        self.ID = ID
        # self.worker = ShoppingItemWorker()
        self.signals = ShoppingItemSignals()
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
        self.widgetText = QLabel(self.widget)
        self.widgetText.setText(self.itemTitle)
        self.widgetText.setFont(font12B)
        self.widgetText.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.widgetText.setStyleSheet("background-color: transparent; color: #7e8198; padding: 0")
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
        self.widgetLayout.addWidget(self.widgetText, 0, 0, 1, 1)
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
        self.signals.signal_add.emit({"title": self.widgetText.text(), "id": self.ID})

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
        # self.worker.signal.emit(self.ID)
        self.signals.signal_remove.emit(self.ID)

class TransactionItemSignals(QObject):
    signal = pyqtSignal()

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
                    "Food": "#b1d672",
                    "Bills": "#7963cd",
                    "Entertainment": "#ff8f78",
                    "Health": "#c13c3c",
                    "Education": "#3dbce0",
                    "Clothes": "#cbb64d",
                    "Salary": "#277a44",
                    "Other Income": "#277a44"}
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
            self.typeTrancLabel.setStyleSheet("background-color: white; color: #51546f; border: transparent; border-radius: 0;")
            tag.setStyleSheet("background-color: #51546f; opacity: 0.5;")

        self.typeTrancLabel.setFont(font12B)
        self.typeTrancLabel.setAlignment(Qt.AlignLeft)
        self.typeTrancLabel.setText(self.type)
        self.costTrancLabel = QLabel(self.widget)
        self.costTrancLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.costTrancLabel.setFont(font12B)
        self.costTrancLabel.setAlignment(Qt.AlignRight)
        if (self.type.lower() == "salary") or (self.type.lower() == "other income"):
            self.costTrancLabel.setStyleSheet("background-color: white; color: #277a44; border: transparent; border-radius: 0;")
            self.costTrancLabel.setText("+ " + currency(cost, brief=True) if cost>=1e6 else "+ " + currency(cost))
        else:
            self.costTrancLabel.setStyleSheet("background-color: white; color: #1d1c1c; border: transparent; border-radius: 0;")
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


# """ ========= AccountWidget ========= """
class AccountWidgetSignals(QObject):
    signal_prevAccount = pyqtSignal()
    signal_nextAccount = pyqtSignal()
    signal_gotoDetailTab = pyqtSignal()
    signal_gotoCardTab = pyqtSignal()

class AccountWidget(QWidget):
    def __init__(self, accountWidget, addDialog, _font, conn):
        super(AccountWidget, self).__init__()
        self.accountWidget = accountWidget
        self.addDialog = addDialog
        self._font = _font
        self.conn = conn
        self.signals = AccountWidgetSignals()
        self.accountWidget.setStyleSheet("border: transparent; background-color: white; border-radius: 15px;")
        # accountWidget.setStyleSheet("border: transparent; background-color: transparent; border-radius: 15px;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountWidget.sizePolicy().hasHeightForWidth())
        self.accountWidget.setSizePolicy(sizePolicy)
        self.accountWidgetLayout = QHBoxLayout(self.accountWidget)
        self.accountWidgetLayout.setSpacing(5)

        self.createColumnWidget0()
        self.createColumnWidget1()

        self.accountWidgetLayout.addWidget(self.accountWidgetColumn0)
        self.accountWidgetLayout.addWidget(self.accountWidgetColumn1)
        self.accountWidgetLayout.setStretch(0, 1)
        self.accountWidgetLayout.setStretch(1, 1)
        accountWidget.setLayout(self.accountWidgetLayout)

    def createColumnWidget0(self):
        self.accountWidgetColumn0 = QWidget(self.accountWidget)
        self.accountWidgetColumn0Layout = QVBoxLayout(self.accountWidgetColumn0)
        self.selectAccoutWidget = QWidget(self.accountWidgetColumn0)
        self.selectAccoutWidgetLayout = QHBoxLayout(self.selectAccoutWidget)
        self.prevAccButton = QPushButton(self.selectAccoutWidget)
        self.prevAccButton.setText("◄")
        self.prevAccButton.setFont(self._font.font14)
        self.prevAccButton.clicked.connect(lambda: self.signals.signal_prevAccount.emit())
        self.prevAccButton.setStyleSheet("""QPushButton{ background-color: #daf2ef; color: #51546f; border: transparent; padding: 10; border-radius: 10; }
                                            QPushButton::pressed{ background-color: #767891; color: #3c3e54; border: transparent; padding: 10; border-radius: 10; }
                                            QPushButton::hover{ background-color: #e1f5f2; color: #7a7c93; border: transparent; padding: 10; border-radius: 10; }""")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevAccButton.sizePolicy().hasHeightForWidth())
        self.prevAccButton.setSizePolicy(sizePolicy)
        self.nameAccountLabel = QLabel(self.selectAccoutWidget)
        self.nameAccountLabel.setText("Main Account")
        self.nameAccountLabel.setFont(self._font.font14B)
        self.nameAccountLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter,)
        self.nameAccountLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameAccountLabel.sizePolicy().hasHeightForWidth())
        self.nameAccountLabel.setSizePolicy(sizePolicy)
        self.nextAccButton = QPushButton(self.selectAccoutWidget)
        self.nextAccButton.setText("►")
        self.nextAccButton.setFont(self._font.font14)
        self.nextAccButton.clicked.connect(lambda: self.signals.signal_nextAccount.emit())
        self.nextAccButton.setStyleSheet("""QPushButton{ background-color: #daf2ef; color: #51546f; border: transparent; padding: 10; border-radius: 10; }
                                            QPushButton::pressed{ background-color: #767891; color: #3c3e54; border: transparent; padding: 10; border-radius: 10; }
                                            QPushButton::hover{ background-color: #e1f5f2; color: #7a7c93; border: transparent; padding: 10; border-radius: 10; }""")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextAccButton.sizePolicy().hasHeightForWidth())
        self.selectAccoutWidgetLayout.addWidget(self.prevAccButton)
        self.selectAccoutWidgetLayout.addWidget(self.nameAccountLabel)
        self.selectAccoutWidgetLayout.addWidget(self.nextAccButton)
        self.selectAccoutWidgetLayout.addItem(QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:15 h:15
        self.selectAccoutWidgetLayout.setStretch(1, 3)
        self.selectAccoutWidgetLayout.setStretch(3, 2)
        self.selectAccoutWidget.setLayout(self.selectAccoutWidgetLayout)

        self.accountTitleLabel = QLabel(self.accountWidgetColumn0)
        self.accountTitleLabel.setFont(self._font.font20B)
        self.accountTitleLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding: 10;")
        
        self.accountbriefLabel = QLabel(self.accountWidgetColumn0)
        self.accountbriefLabel.setFont(self._font.font12B)
        self.accountbriefLabel.setAlignment(Qt.AlignTop)
        self.accountbriefLabel.setStyleSheet("background-color: transparent; color: #757890; border: transparent; padding: 10;")

        self.navigatorWidget = QWidget(self.accountWidgetColumn0)
        self.navigatorWidgetLayout = QHBoxLayout(self.navigatorWidget)
        self.gotoDetailTabButn = QPushButton(self.navigatorWidget)
        self.gotoDetailTabButn.setFont(self._font.font14B)
        self.gotoDetailTabButn.setText("Details")
        self.gotoDetailTabButn.clicked.connect(lambda: self.signals.signal_gotoDetailTab.emit())
        self.gotoDetailTabButn.setStyleSheet("""QPushButton{ background-image: url(image/button-icon-enabled.png); background-position: center; background-color: #058373; color: #d5e9e7; border: transparent; padding: 20; border-radius: 20; }
                                                QPushButton::disabled{ background-image: url(image/button-icon-disabled.png); background-color: #f2f3f8; color: #a7a9b5; border: transparent; padding: 20; border-radius: 20; }
                                                QPushButton::hover{ background-color: #10a391; color: #d3e3e1; border: transparent; padding: 20; border-radius: 20; }""")
        self.gotoCardTabButn = QPushButton(self.navigatorWidget)
        self.gotoCardTabButn.setFont(self._font.font14B)
        self.gotoCardTabButn.setText("Card Information")
        self.gotoCardTabButn.clicked.connect(lambda: self.signals.signal_gotoCardTab.emit())
        self.gotoCardTabButn.setStyleSheet("""QPushButton{ background-image: url(image/button-icon-enabled.png); background-color: #058373; color: #d5e9e7; border: transparent; padding: 20; border-radius: 20; }
                                                QPushButton::disabled{ background-image: url(image/button-icon-disabled.png); background-color: #f2f3f8; color: #a7a9b5; border: transparent; padding: 20; border-radius: 20; }
                                                QPushButton::hover{ background-color: #10a391; color: #d3e3e1; border: transparent; padding: 20; border-radius: 20; }""")
        self.gotoCardTabButn.setEnabled(False)
        self.navigatorWidgetLayout.addWidget(self.gotoDetailTabButn)
        self.navigatorWidgetLayout.addWidget(self.gotoCardTabButn)
        self.navigatorWidgetLayout.addItem(QSpacerItem(5, 5, QSizePolicy.Expanding, QSizePolicy.Maximum)) # w:15 h:15
        self.navigatorWidgetLayout.setStretch(0, 2)
        self.navigatorWidgetLayout.setStretch(1, 2)
        self.navigatorWidgetLayout.setStretch(2, 1)
        self.navigatorWidget.setLayout(self.navigatorWidgetLayout)

        self.accountWidgetColumn0Layout.addWidget(self.selectAccoutWidget)
        self.accountWidgetColumn0Layout.addWidget(self.accountTitleLabel)
        self.accountWidgetColumn0Layout.addWidget(self.accountbriefLabel)
        self.accountWidgetColumn0Layout.addWidget(self.navigatorWidget)
        self.accountWidgetColumn0Layout.setStretch(0, 0)
        self.accountWidgetColumn0Layout.setStretch(1, 2)
        self.accountWidgetColumn0Layout.setStretch(2, 2)
        self.accountWidgetColumn0Layout.setStretch(3, 2)
        self.accountWidgetColumn0.setLayout(self.accountWidgetColumn0Layout)

    def createColumnWidget1(self):
        self.accountWidgetColumn1 = QWidget(self.accountWidget)
        self.accountWidgetColumn1Layout = QGridLayout(self.accountWidgetColumn1)
        self.accountWidgetColumn1Layout.setSpacing(0)
        self.availBalanceTextLabel = QLabel(self.accountWidgetColumn1)
        self.availBalanceTextLabel.setText("Available balance")
        self.availBalanceTextLabel.setFont(self._font.font12B)
        self.availBalanceTextLabel.setAlignment(Qt.AlignRight)
        self.availBalanceTextLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")
        
        self.colorTagAvailBalance = QFrame(self.accountWidgetColumn1)
        self.colorTagAvailBalance.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.colorTagAvailBalance.setFixedWidth(10)
        self.colorTagAvailBalance.setStyleSheet("background-color: #41ab2e; color: #41ab2e")

        self.availBalanceLabel = QLabel(self.accountWidgetColumn1)
        self.availBalanceLabel.setText(currency(31076464))
        self.availBalanceLabel.setFont(self._font.font30BU)
        self.availBalanceLabel.setAlignment(Qt.AlignRight)
        self.availBalanceLabel.setStyleSheet("background-color: transparent; color: #2f5240; border: transparent; padding: 10;")
        
        self.expenseTextLabel = QLabel(self.accountWidgetColumn1)
        self.expenseTextLabel.setText("Expenses")
        self.expenseTextLabel.setFont(self._font.font12B)
        self.expenseTextLabel.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.expenseTextLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")

        self.expenseLabel = QLabel(self.accountWidgetColumn1)
        self.expenseLabel.setText(currency(2200000, brief=True))
        self.expenseLabel.setFont(self._font.font24B)
        self.expenseLabel.setAlignment(Qt.AlignRight)
        self.expenseLabel.setStyleSheet("background-color: transparent; color: #102a3b; border: transparent; padding: 10;")

        self.colorTagExpenses = QFrame(self.accountWidgetColumn1)
        self.colorTagExpenses.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.colorTagExpenses.setFixedHeight(self.expenseTextLabel.height()*2 + self.expenseLabel.height())
        self.colorTagExpenses.setFixedWidth(10)
        self.colorTagExpenses.setStyleSheet("background-color: #4791bf; color: #4791bf")

        self.incomeTextLabel = QLabel(self.accountWidgetColumn1)
        self.incomeTextLabel.setText("Income")
        self.incomeTextLabel.setFont(self._font.font12B)
        self.incomeTextLabel.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.incomeTextLabel.setStyleSheet("background-color: transparent; color: #74778f; border: transparent; padding: 10;")

        self.incomeLabel = QLabel(self.accountWidgetColumn1)
        self.incomeLabel.setText(currency(10000000, brief=True))
        self.incomeLabel.setFont(self._font.font24B)
        self.incomeLabel.setAlignment(Qt.AlignRight)
        self.incomeLabel.setStyleSheet("background-color: transparent; color: #4d340b; border: transparent; padding: 10;")

        self.colorTagIncome = QFrame(self.accountWidgetColumn1)
        self.colorTagIncome.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.colorTagIncome.setFixedHeight(self.incomeTextLabel.height()*2 + self.incomeLabel.height())
        self.colorTagIncome.setFixedWidth(10)
        self.colorTagIncome.setStyleSheet("background-color: #e39517; color: #e39517")

        self.accountWidgetColumn1Layout.addWidget(self.availBalanceTextLabel, 0, 0, 1, 4)
        self.accountWidgetColumn1Layout.addWidget(self.availBalanceLabel, 1, 0, 1, 4)
        self.accountWidgetColumn1Layout.addWidget(self.colorTagAvailBalance, 0, 4, 2, 1)
        self.accountWidgetColumn1Layout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum))
        self.accountWidgetColumn1Layout.addWidget(self.expenseTextLabel, 3, 0, 1, 1)
        self.accountWidgetColumn1Layout.addWidget(self.expenseLabel, 4, 0, 1, 1)
        self.accountWidgetColumn1Layout.addWidget(self.colorTagExpenses, 3, 1, 2, 1)
        self.accountWidgetColumn1Layout.addWidget(self.incomeTextLabel, 3, 3, 1, 1)
        self.accountWidgetColumn1Layout.addWidget(self.incomeLabel, 4, 3, 1, 1)
        self.accountWidgetColumn1Layout.addWidget(self.colorTagIncome, 3, 4, 2, 1)
        self.accountWidgetColumn1.setLayout(self.accountWidgetColumn1Layout)

    def reload(self, signals):
        self.accountbriefLabel.setText(signals["brief"])
        availableBalance = self.conn.querySumIncome() - self.conn.querySumExpenses()
        self.availBalanceLabel.setText(currency(availableBalance))
        totalExpense = self.conn.querySumExpenses(_from = signals["from"] if signals is not None else None,
                                                    _to = signals["to"] if signals is not None else None)
        self.expenseLabel.setText(currency(totalExpense, brief=True))
        totalIncome = self.conn.querySumIncome(_from = signals["from"] if signals is not None else None,
                                                    _to = signals["to"] if signals is not None else None)
        self.incomeLabel.setText(currency(totalIncome, brief=True))


# """ ========= ShopTodayWidget ========= """
class ShopTodayWidgetSignals(QObject):
    signal_addShopToday = pyqtSignal()

class ShopTodayWidget(QWidget):
    def __init__(self, shopTodayWidget, addDialog, addShoppingItemDialog, _font, conn):
        super(ShopTodayWidget, self).__init__()
        self.shopTodayWidget = shopTodayWidget
        self.addDialog = addDialog
        self.addShoppingItemDialog = addShoppingItemDialog
        self._font = _font
        self.conn = conn
        self.signals = ShopTodayWidgetSignals()
        self.shopTodayWidget.setStyleSheet("border: transparent; background-color: #058272; border-radius: 15px;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shopTodayWidget.sizePolicy().hasHeightForWidth())
        self.shopTodayWidget.setSizePolicy(sizePolicy)
        self.shopTodayWidgetLayout = QGridLayout(self.shopTodayWidget)
        self.shopTodayWidgetLayout.setSpacing(5)
        self.shopTodayTitleLabel = QLabel(self.shopTodayWidget)
        self.shopTodayTitleLabel.setText("Shopping List")
        self.shopTodayTitleLabel.setFont(self._font.font16B)
        self.shopTodayTitleLabel.setAlignment(Qt.AlignLeft)
        self.shopTodayTitleLabel.setStyleSheet("background-color: transparent; color: #dbedeb; border: transparent; padding: 10;")
        self.shopTodayTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.plusButton = QPushButton(self.shopTodayWidget)
        self.plusButton.setText(" Add ")
        self.plusButton.setFont(self._font.font14B)
        self.plusButton.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.plusButton.setMaximumWidth(70)
        self.plusButton.clicked.connect(self.plusButtonHandle)
        self.plusButton.setStyleSheet("""QPushButton{ background-color: #ff8f78; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                    QPushButton::pressed{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                    QPushButton::hover{ background-color: #ffb274; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }""")

        self.calendarIcon = QLabel(self.shopTodayWidget)
        self.calendarIcon.setFixedSize(30, 42)
        self.calendarIcon.setStyleSheet("background-color: transparent; border: transparent;")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarIcon.sizePolicy().hasHeightForWidth())
        self.calendarIcon.setSizePolicy(sizePolicy)
        self.calendarIcon.setPixmap(QPixmap("image/favpng_e-commerce-online-shopping-icon.png").scaled(self.calendarIcon.width(), 
                                    self.calendarIcon.height(), Qt.KeepAspectRatio, Qt.FastTransformation))

        self.shoppingListWidget = QListWidget(self.shopTodayWidget)
        self.shoppingListItems = []

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shoppingListWidget.sizePolicy().hasHeightForWidth())
        self.shoppingListWidget.setSizePolicy(sizePolicy)
        self.shoppingListWidget.setStyleSheet("background-color: transparent; color: #dbedeb; border: transparent; padding: 10;")

        self.reload()

        self.paddingWidget = QWidget(self.shopTodayWidget)
        self.paddingWidgetLayout = QHBoxLayout(self.paddingWidget)
        self.paddingWidgetLayout.setSpacing(10)
        self.paddingWidgetLayout.addWidget(self.shoppingListWidget)
        self.paddingWidget.setLayout(self.paddingWidgetLayout)

        self.shopTodayWidgetLayout.addWidget(self.shopTodayTitleLabel, 0, 0, 1, 1)
        self.shopTodayWidgetLayout.addWidget(self.plusButton, 0, 1, 1, 1)
        self.shopTodayWidgetLayout.addWidget(self.calendarIcon, 0, 2, 1, 1)
        self.shopTodayWidgetLayout.addWidget(self.paddingWidget, 1, 0, 1, 3)
        self.shopTodayWidgetLayout.setColumnStretch(0, 10)

        shopTodayWidget.setLayout(self.shopTodayWidgetLayout)

    def addNew(self, _title, _id=None):
        if _id is None:
            _id = self.conn.insertRowShoppingList(_title)
        
        item = ShoppingItem(self.shoppingListWidget, _title, _id)
        item.insert(top=True)
        item.signals.signal_remove.connect(self.conn.deleteRowShoppingList)
        item.signals.signal_add.connect(partial(self.shopTodayDone, {"title": _title, "id": _id}))
        self.shoppingListItems.append(item)

    def reload(self, signals=None):
        for i in range(len(self.shoppingListItems) - 1, -1 , -1):
            del(self.shoppingListItems[i])

        self.shoppingListWidget.clear()
        self.shoppingListItems.clear()
        shoppingList = self.conn.queryRowsShoppingList()
        for _id, _title in shoppingList:
            self.addNew(_title, _id)

    def shopTodayDone(self, signals):
        self.addDialog.signals.signal_requestShow.emit({"title":signals["title"], "now":datetime.now()})
        self.conn.deleteRowShoppingList(signals["id"])

    def plusButtonHandle(self):
        self.addShoppingItemDialog.show()


# """ ========= LatestTrancWidget ========= """
class LatestTrancWidgetSignals(QObject):
    signal_gotoDetailTab = pyqtSignal()

class LatestTrancWidget(QWidget):
    def __init__(self, latestTrancWidget, addDialog, _font, conn):
        super(LatestTrancWidget, self).__init__()
        self.latestTrancWidget = latestTrancWidget
        self.addDialog = addDialog
        self._font = _font
        self.conn = conn
        self.signals = LatestTrancWidgetSignals()
        self.latestTrancWidget.setStyleSheet("border: transparent; background-color: white; border-radius: 15px;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latestTrancWidget.sizePolicy().hasHeightForWidth())
        self.latestTrancWidget.setSizePolicy(sizePolicy)
        self.latestTrancWidgetLayout = QGridLayout(self.latestTrancWidget)
        self.latestTrancWidgetLayout.setSpacing(0)

        self.createRowWidget0()
        self.createRowWidget1()

        self.latestTrancWidgetLayout.addWidget(self.latestTrancWidget_row0)
        self.latestTrancWidgetLayout.addWidget(self.padding2)
        self.latestTrancWidgetLayout.addWidget(self.latestTrancWidget_row1)
        self.latestTrancWidget.setLayout(self.latestTrancWidgetLayout)

    def createRowWidget0(self):
        self.latestTrancWidget_row0 = QWidget(self.latestTrancWidget)
        self.latestTrancWidget_row0Layout = QHBoxLayout(self.latestTrancWidget_row0)
        self.latestTrancTitleLabel = QLabel(self.latestTrancWidget_row0)
        self.latestTrancTitleLabel.setText("Latest transactions")
        self.latestTrancTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.latestTrancTitleLabel.setFont(self._font.font16B)
        self.latestTrancTitleLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10;")
        self.addNewButn = QPushButton(self.latestTrancWidget_row0)
        self.addNewButn.setText("+")
        self.addNewButn.setFixedWidth(50)
        self.addNewButn.setFont(self._font.font20B)
        self.addNewButn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.addNewButn.clicked.connect(lambda: self.addDialog.signals.signal_requestShow.emit({"title":"", "now":datetime.now()}))
        self.addNewButn.setStyleSheet("""QPushButton{ background-color: #058373; color: #cfe7e4; border: transparent; padding: 5; border-radius: 10; }
                                                QPushButton:hover{ background-color: #0eab97; color: #c3e3df; border: transparent; padding: 5; border-radius: 10; }""")
        self.moreDetailTabButn2 = QPushButton(self.latestTrancWidget_row0)
        self.moreDetailTabButn2.setText("➔")
        self.moreDetailTabButn2.setFixedWidth(50)
        self.moreDetailTabButn2.setFont(self._font.font14B)
        self.moreDetailTabButn2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.moreDetailTabButn2.clicked.connect(lambda: self.signals.signal_gotoDetailTab.emit())
        self.moreDetailTabButn2.setStyleSheet("""QPushButton{ background-color: #058373; color: #cfe7e4; border: transparent; padding: 10; border-radius: 10; }
                                                QPushButton:hover{ background-color: #0eab97; color: #c3e3df; border: transparent; padding: 10; border-radius: 10; }""")
        self.latestTrancWidget_row0Layout.addWidget(self.latestTrancTitleLabel)
        self.latestTrancWidget_row0Layout.addWidget(self.addNewButn)
        self.latestTrancWidget_row0Layout.addWidget(self.moreDetailTabButn2)
        self.latestTrancWidget_row0.setLayout(self.latestTrancWidget_row0Layout)

        self.hSeparator = QWidget(self.latestTrancWidget)
        self.hSeparator.setFixedHeight(2)
        self.hSeparator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.hSeparator.setStyleSheet("background-color: #eaebec; padding-left: 10px; padding-right: 10px")
        self.padding = QWidget(self.latestTrancWidget)
        self.paddingLayout = QHBoxLayout(self.padding)
        self.padding.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.padding.setStyleSheet("background-color: transparent")
        self.paddingLayout.addWidget(self.hSeparator)
        self.padding.setLayout(self.paddingLayout)
        self.padding2 = QWidget(self.latestTrancWidget)
        self.padding2Layout = QHBoxLayout(self.padding2)
        self.padding2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.padding2.setStyleSheet("background-color: transparent")
        self.padding2Layout.addWidget(self.padding)
        self.padding2.setLayout(self.padding2Layout)

    def createRowWidget1(self):
        self.latestTrancWidget_row1 = QWidget(self.latestTrancWidget)
        self.latestTrancWidget_row1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.latestTrancWidget_row1Layout = QHBoxLayout(self.latestTrancWidget_row1)
        self.latestTrancWidget_row1.setLayout(self.latestTrancWidget_row1Layout)
        self.trancListWidget = QListWidget(self.latestTrancWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trancListWidget.sizePolicy().hasHeightForWidth())
        self.trancListWidget.setSizePolicy(sizePolicy)
        self.trancListWidget.setStyleSheet("background-color: transparent; color: #dbedeb; border: transparent; border-radius: 0px;")
        self.trancListItems = []
        
        self.reload()

        self.latestTrancWidget_row1Layout.addWidget(self.trancListWidget)
        self.latestTrancWidget_row1.setLayout(self.latestTrancWidget_row1Layout)

    def _func(self, date):
        date = datetime.fromtimestamp(date)
        date = datetime(year=date.year, month=date.month, day=date.day)
        now = datetime.now()
        now = datetime(year=now.year, month=now.month, day=now.day)
        if (now - date).days == 0:
            return "Today"
        elif (now - date).days == 1:
            return "Yesterday"
        else:
            return "{}.{}.{}".format(str(date.year)[2:], str(date.month).zfill(2), str(date.day).zfill(2))

    def addNew(self, _timeTranc, _titleTranc, _payment, _type, _cost, _id=None):
        if _id is None:
            _id = self.conn.insertRowTransactions(_timeTranc, _titleTranc, _payment, _type, _cost)

        item = TransactionItem(self.trancListWidget, _id, self._func(_timeTranc), _titleTranc, _payment, _type, _cost)
        item.insert(top=True)
        self.trancListItems.append(item)

    def reload(self, signals=None):
        for i in range(len(self.trancListItems) - 1, -1 , -1): del(self.trancListItems[i])

        self.trancListWidget.clear()
        self.trancListItems.clear()
        
        for _id, _timeTranc, _titleTranc, _payment, _type, _cost in \
                    self.conn.queryRowsTransactions(_from = signals["from"] if signals is not None else None,
                                                        _to = signals["to"] if signals is not None else None):
            self.addNew(_timeTranc, _titleTranc, _payment, _type, _cost, _id)
            

# """ ========= AllExpensesWidget ========= """
class AllExpensesWidgetSignals(QObject):
    signal_gotoDetailTab = pyqtSignal()
    signal_updateInfoAll = pyqtSignal(dict)

class AllExpensesWidget(QWidget):
    ItemsContent = ["all", "this month", "last month", "this year", "last year", "custom"]
    def __init__(self, allExpensesWidget, addDialog, _font, conn): 
        super(AllExpensesWidget, self).__init__()
        self.allExpensesWidget = allExpensesWidget
        self.addDialog = addDialog
        self._font = _font
        self.conn = conn
        self.signals = AllExpensesWidgetSignals()
        self.allExpensesWidget.setStyleSheet("border: transparent; background-color: white; border-radius: 15px;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allExpensesWidget.sizePolicy().hasHeightForWidth())
        self.allExpensesWidget.setSizePolicy(sizePolicy)
        self.allExpensesWidgetLayout = QVBoxLayout(self.allExpensesWidget)
        
        self.createRowWidget0()
        self.createRowWidget1()
        self.createRowWidget2()

        self.allExpensesWidgetLayout.addWidget(self.allExpensesWidget_row0)
        self.allExpensesWidgetLayout.addWidget(self.allExpensesWidget_row1)
        self.allExpensesWidgetLayout.addWidget(self.padding2)
        self.allExpensesWidgetLayout.addWidget(self.allExpensesWidget_row2)
        self.allExpensesWidgetLayout.setStretch(0, 1)
        self.allExpensesWidgetLayout.setStretch(1, 1)
        self.allExpensesWidgetLayout.setStretch(3, 5)
        self.allExpensesWidget.setLayout(self.allExpensesWidgetLayout)

    def createRowWidget0(self):
        self.allExpensesWidget_row0 = QWidget(self.allExpensesWidget)
        self.allExpensesWidget_row0Layout = QHBoxLayout(self.allExpensesWidget_row0)
        self.allExpensesTitleLabel = QLabel(self.allExpensesWidget_row0)
        self.allExpensesTitleLabel.setText("All expenses")
        self.allExpensesTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.allExpensesTitleLabel.setFont(self._font.font16B)
        self.allExpensesTitleLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10;")
        self.gotoDetailTabButn2 = QPushButton(self.allExpensesWidget_row0)
        self.gotoDetailTabButn2.setText("➔")
        self.gotoDetailTabButn2.setFont(self._font.font14B)
        self.gotoDetailTabButn2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.gotoDetailTabButn2.clicked.connect(lambda: self.signals.signal_gotoDetailTab.emit())
        self.gotoDetailTabButn2.setStyleSheet("""QPushButton{ background-color: #058373; color: #cfe7e4; border: transparent; padding: 10; border-radius: 10; }
                                                    QPushButton:hover{ background-color: #0eab97; color: #c3e3df; border: transparent; padding: 10; border-radius: 10; }""")
        self.allExpensesWidget_row0Layout.addWidget(self.allExpensesTitleLabel)
        self.allExpensesWidget_row0Layout.addWidget(self.gotoDetailTabButn2)
        self.allExpensesWidget_row0.setLayout(self.allExpensesWidget_row0Layout)

    def createRowWidget1(self):
        self.allExpensesWidget_row1 = QWidget(self.allExpensesWidget)
        self.allExpensesWidget_row1Layout = QGridLayout(self.allExpensesWidget_row1)
        self.dailyTitleLabel = QLabel(self.allExpensesWidget_row1)
        self.dailyTitleLabel.setText("daily")
        self.dailyTitleLabel.setAlignment(Qt.AlignLeft)
        self.dailyTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.dailyTitleLabel.setFont(self._font.font12B)
        self.dailyTitleLabel.setStyleSheet("background-color: transparent; color: #72758e; border: transparent; padding-left: 10; padding-bottom: 0;")
        self.weeklyTitleLabel = QLabel(self.allExpensesWidget_row1)
        self.weeklyTitleLabel.setText("weekly")
        self.weeklyTitleLabel.setAlignment(Qt.AlignLeft)
        self.weeklyTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.weeklyTitleLabel.setFont(self._font.font12B)
        self.weeklyTitleLabel.setStyleSheet("background-color: transparent; color: #72758e; border: transparent; padding-left: 10; padding-bottom: 0;")
        self.monthlyTitleLabel = QLabel(self.allExpensesWidget_row1)
        self.monthlyTitleLabel.setText("monthly")
        self.monthlyTitleLabel.setAlignment(Qt.AlignLeft)
        self.monthlyTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.monthlyTitleLabel.setFont(self._font.font12B)
        self.monthlyTitleLabel.setStyleSheet("background-color: transparent; color: #72758e; border: transparent; padding-left: 10; padding-bottom: 0;")
        self.dailyLabel = QLabel(self.allExpensesWidget_row1)
        self.dailyLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.dailyLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.dailyLabel.setFont(self._font.font18B)
        self.dailyLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10; padding-bottom: 0;")
        self.weeklyLabel = QLabel(self.allExpensesWidget_row1)
        self.weeklyLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.weeklyLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.weeklyLabel.setFont(self._font.font18B)
        self.weeklyLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10; padding-bottom: 0;")
        self.monthlyLabel = QLabel(self.allExpensesWidget_row1)
        self.monthlyLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.monthlyLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.monthlyLabel.setFont(self._font.font18B)
        self.monthlyLabel.setStyleSheet("background-color: transparent; color: #1d1c1c; border: transparent; padding-left: 10; padding-bottom: 0;")
        self.allExpensesWidget_row1Layout.addWidget(self.dailyTitleLabel, 0, 0, 1, 1)
        self.allExpensesWidget_row1Layout.addWidget(self.weeklyTitleLabel, 0, 1, 1, 1)
        self.allExpensesWidget_row1Layout.addWidget(self.monthlyTitleLabel, 0, 2, 1, 1)
        self.allExpensesWidget_row1Layout.addWidget(self.dailyLabel, 1, 0, 1, 1)
        self.allExpensesWidget_row1Layout.addWidget(self.weeklyLabel, 1, 1, 1, 1)
        self.allExpensesWidget_row1Layout.addWidget(self.monthlyLabel, 1, 2, 1, 1)
        self.allExpensesWidget_row1.setLayout(self.allExpensesWidget_row1Layout)

    def createRowWidget2(self):
        self.allExpensesWidget_row2 = QWidget(self.allExpensesWidget)
        self.allExpensesWidget_row2Layout = QVBoxLayout(self.allExpensesWidget_row2)
        self.durationComboBox = QComboBox(self.allExpensesWidget_row2)
        self.durationComboBox.setFont(self._font.font12B)
        self.durationComboBox.setStyleSheet("""QComboBox{ background-color: transparent; padding-left: 15px }
                                            QComboBox:QAbstractItemView{ background-color: white; color:orange; padding-left: 15px }""")
        self.durationComboBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        for itemContent in self.ItemsContent:
            self.durationComboBox.addItem(itemContent)

        self.durationComboBox.activated[str].connect(self.onActivated)
        self.chart = QChart()
        self.chartview = QChartView(self.chart)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chartview.setRenderHint(QPainter.Antialiasing)

        self.allExpensesWidget_row2Layout.addWidget(self.durationComboBox)
        self.allExpensesWidget_row2Layout.addWidget(self.chartview)
        self.allExpensesWidget_row2.setLayout(self.allExpensesWidget_row2Layout)

        self.hSeparator = QWidget(self.allExpensesWidget)
        self.hSeparator.setFixedHeight(2)
        self.hSeparator.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.hSeparator.setStyleSheet("background-color: #eaebec; padding-left: 10px; padding-left: 10px")
        self.padding = QWidget(self.allExpensesWidget)
        self.paddingLayout = QHBoxLayout(self.padding)
        self.padding.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.padding.setStyleSheet("background-color: transparent")
        self.paddingLayout.addWidget(self.hSeparator)
        self.padding.setLayout(self.paddingLayout)
        self.padding2 = QWidget(self.allExpensesWidget)
        self.padding2Layout = QHBoxLayout(self.padding2)
        self.padding2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.padding2.setStyleSheet("background-color: transparent")
        self.padding2Layout.addWidget(self.padding)
        self.padding2.setLayout(self.padding2Layout)

    def createChart(self, signals):
        r = self.conn.querySumExpensesInEachTag(_from = signals["from"] if signals is not None else None,
                                                    _to = signals["to"] if signals is not None else None)
        tag = [_r[0] for _r in r]
        data = [_r[1] for _r in r]
        color = [TRANCS_TAG[t] for t in tag]
        self.chart.removeAllSeries()
        series = QPieSeries()
        series.setHoleSize(0.6)
        for _data, _tag, _color in zip(data, tag, color):
            series.append(_tag, _data)
            slice = QPieSlice()
            slice = series.slices()[series.count() - 1]
            # slice.setExploded(True)
            slice.setLabel("{}: {}".format(_tag, currency(_data, "", brief=True)))
            slice.setLabelFont(self._font.font10BI)
            slice.setLabelVisible(True)
            slice.setPen(QPen(QColor(_color), 0))
            slice.setBrush(QColor(_color))

        self.chart.addSeries(series)
        self.chart.legend().setAlignment(Qt.AlignRight)
        for i, _tag in enumerate(tag):
            self.chart.legend().markers(series)[i].setLabel(_tag)
            self.chart.legend().markers(series)[i].setFont(self._font.font10B)

    def dateConvention(self, date):
        return "{}, {}{} {}".format(MONTH[date.month],
                                    date.day,
                                    "st" if date.day in [1, 21, 31] \
                                        else "nd" \
                                            if date.day in [2, 22] \
                                                else "rd" \
                                                    if date.day in [3, 23] \
                                                        else "th",
                                    str(date.year))

    def onActivated(self, text):
        if text == "all":
            timeline_from = datetime.fromtimestamp(self.conn.queryMinTransactionTime())
            timeline_to = datetime.now()
            self.signals.signal_updateInfoAll.emit({"brief":"from {} to now".format(self.dateConvention(timeline_from)),
                                                    "from": timeline_from.timestamp(),
                                                    "to": timeline_to.timestamp()})
        elif text == "this month":
            now = datetime.now()
            timeline_from = datetime(year=now.year, month=now.month, day=1)
            # timeline_to = (datetime(year=now.year, month=now.month + 1, day=1) if now.month != 12 \
            #                 else datetime(year=now.year+1, month=1, day=1)) \
            #                 - timedelta(seconds=1)
            timeline_to = now
            self.signals.signal_updateInfoAll.emit({"brief":"from {} to now".format(self.dateConvention(timeline_from)),
                                                    "from": timeline_from.timestamp(),
                                                    "to": timeline_to.timestamp()})
        elif text == "last month":
            now = datetime.now()
            timeline_to = datetime(year=now.year, month=now.month, day=1) - timedelta(seconds=1)
            timeline_from = datetime(year=timeline_to.year, month=timeline_to.month, day=1)
            self.signals.signal_updateInfoAll.emit({"brief":"from {} to {}".format(self.dateConvention(timeline_from), \
                                                                                    self.dateConvention(timeline_to)),
                                                    "from": timeline_from.timestamp(),
                                                    "to": timeline_to.timestamp()})
        elif text == "this year":
            now = datetime.now()
            timeline_from = datetime(year=now.year, month=1, day=1)
            timeline_to = datetime.now()
            self.signals.signal_updateInfoAll.emit({"brief":"from {} to now".format(self.dateConvention(timeline_from)),
                                                    "from": timeline_from.timestamp(),
                                                    "to": timeline_to.timestamp()})
        elif text == "last year":
            now = datetime.now()
            timeline_to = datetime(year=now.year, month=1, day=1) - timedelta(seconds=1)
            timeline_from = datetime(year=timeline_to.year, month=1, day=1)
            self.signals.signal_updateInfoAll.emit({"brief":"from {} to {}".format(self.dateConvention(timeline_from), \
                                                                                    self.dateConvention(timeline_to)),
                                                    "from": timeline_from.timestamp(),
                                                    "to": timeline_to.timestamp()})
        elif text == "custom":
            timeline_from = datetime(year=2020, month=5, day=14)
            timeline_to = datetime(year=2020, month=10, day=22) - timedelta(seconds=1) + timedelta(days=1)
            self.signals.signal_updateInfoAll.emit({"brief":"from {} to {}".format(self.dateConvention(timeline_from), \
                                                                                    self.dateConvention(timeline_to)),
                                                    "from": timeline_from.timestamp(),
                                                    "to": timeline_to.timestamp()})
        else:
            return

    def reload(self, signals):
        self.createChart(signals=signals)
        _now = datetime.now()

        dailyExpenses = self.conn.querySumExpenses(_from=datetime(_now.year, _now.month, _now.day).timestamp(),
                                    _to=(datetime(_now.year, _now.month, _now.day) + timedelta(days=1) - timedelta(seconds=1)).timestamp())

        weeklyExpenses = self.conn.querySumExpenses(_from=(datetime(_now.year, _now.month, _now.day) - timedelta(days=_now.weekday())).timestamp(),
                                    _to=(datetime(_now.year, _now.month, _now.day) + timedelta(days=7 - _now.weekday()) - timedelta(seconds=1)).timestamp())

        monthlyExpenses = self.conn.querySumExpenses(_from=datetime(_now.year, _now.month, 1).timestamp(),
                                    _to=((datetime(year=_now.year, month=_now.month + 1, day=1) if _now.month != 12 \
                                                else datetime(year=_now.year+1, month=1, day=1)) \
                                                - timedelta(seconds=1)).timestamp())
        self.dailyLabel.setText(currency(dailyExpenses, brief=True))
        self.weeklyLabel.setText(currency(weeklyExpenses, brief=True))
        self.monthlyLabel.setText(currency(monthlyExpenses, brief=True))


# """ ========= AddDialog ========= """
class AddDialogSignals(QObject):
    signal_addNewTranc = pyqtSignal()
    signal_requestShow = pyqtSignal(dict)

class Message(QDialog):
    def __init__(self, app, _font):
        super(Message, self).__init__()
        self._font = _font
        self.setStyleSheet("""QDialog { 
                background-image: url(image/contour-dark-blue-lines-white.jpg);
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 40;
            }""")
        self.setWindowTitle("MyApp!")
        self.setGeometry(QStyle.alignedRect(\
                            Qt.LeftToRight,
                            Qt.AlignCenter,
                            QSize(app.primaryScreen().availableGeometry().width()//3,   
                                    app.primaryScreen().availableGeometry().height()//4),
                        app.desktop().availableGeometry()));
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint);
        self.widgetDialogLayout = QVBoxLayout(self)

        self.message = QLabel(self)
        self.message.setFont(self._font.font14B)
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setStyleSheet("background-color: transparent; color: #db3a2e;")
        self.message.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.createRowWidget2()

        self.widgetDialogLayout.addWidget(self.message)
        self.widgetDialogLayout.addWidget(self.rowWidget2)
        
        self.setLayout(self.widgetDialogLayout)

    def createRowWidget2(self):
        self.rowWidget2 = QWidget(self)
        self.rowWidget2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.rowWidget2Layout = QHBoxLayout(self.rowWidget2)

        self.okButton = QPushButton(self.rowWidget2)
        self.okButton.setText("OK")
        self.okButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.okButton.clicked.connect(self.okButtonHandle)
        self.okButton.setFont(self._font.font16B)
        self.okButton.setStyleSheet("""QPushButton{ background-image: url(image/button-icon-enabled.png); background-color: #058373; color: #d5e9e7; border: transparent; padding: 20; border-radius: 20; }
                                        QPushButton::disabled{ background-image: url(image/button-icon-disabled.png); background-color: #f2f3f8; color: #a7a9b5; border: transparent; padding: 20; border-radius: 20; }
                                        QPushButton::hover{ background-color: #10a391; color: #d3e3e1; border: transparent; padding: 20; border-radius: 20; }""")

        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.addWidget(self.okButton)
        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.setStretch(0, 3)
        self.rowWidget2Layout.setStretch(1, 2)
        self.rowWidget2Layout.setStretch(2, 3)
        self.rowWidget2.setLayout(self.rowWidget2Layout)

    def okButtonHandle(self):
        self.close()

    def show(self, message):
        self.message.setText(message)
        self.exec_()

    def _closeDialogEvent(self, event):
        pass

class AddDialog(QDialog):
    def __init__(self, app, conn, _font):
        super(AddDialog, self).__init__()
        self.conn = conn
        self._font = _font
        self.setStyleSheet("""QDialog { 
                background-image: url(image/contour-lines-cyan-dark-blue.jpg);
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 40;
            }""")
        self.setWindowTitle("MyApp!")
        self.setGeometry(QStyle.alignedRect(\
                            Qt.LeftToRight,
                            Qt.AlignCenter,
                            QSize(app.primaryScreen().availableGeometry().width()//2, 
                                    app.primaryScreen().availableGeometry().height()//2),
                        app.desktop().availableGeometry()));
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint);
        self.message = Message(app, self._font)
        self.signals = AddDialogSignals()
        self.signals.signal_requestShow.connect(self.requestShow)
        self.widgetDialogLayout = QVBoxLayout(self)

        self.dialogTitle = QLabel(self)
        self.dialogTitle.setFont(self._font.font20B)
        self.dialogTitle.setAlignment(Qt.AlignCenter)
        self.dialogTitle.setText("NEW TRANSACTION")
        self.dialogTitle.setStyleSheet("background-color: transparent; color: #f0f0f0;")
        self.dialogTitle.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.createRowWidget0()
        self.createRowWidget1()
        self.createRowWidget2()
        # self.notificationLabel = QLabel(self)

        self.widgetDialogLayout.addWidget(self.dialogTitle)
        self.widgetDialogLayout.addWidget(self.rowWidget0)
        self.widgetDialogLayout.addWidget(self.rowWidget1)
        self.widgetDialogLayout.addWidget(self.rowWidget2)
        self.setLayout(self.widgetDialogLayout)
        self.closeEvent = self._closeDialogEvent

    def createRowWidget0(self):
        self.rowWidget0 = QWidget(self)
        self.rowWidget0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.rowWidget0Layout = QHBoxLayout(self.rowWidget0)
        self.rowWidget0Layout.setSpacing(5)

        self.trancTitle = QLineEdit(self.rowWidget0)
        self.trancTitle.setFont(self._font.font16B)
        self.trancTitle.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px; padding: 15px;")
        self.trancTitle.setPlaceholderText("Transaction")
        self.trancTitle.setAlignment(Qt.AlignCenter)

        self.amount = QLineEdit(self.rowWidget0)
        self.amount.setFont(self._font.font16B)
        self.amount.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px; padding: 15px;")
        self.amount.setPlaceholderText("Cost")
        self.amount.setAlignment(Qt.AlignCenter)

        self.rowWidget0Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget0Layout.addWidget(self.trancTitle)
        self.rowWidget0Layout.addWidget(self.amount)
        self.rowWidget0Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget0Layout.setStretch(0, 1)
        self.rowWidget0Layout.setStretch(1, 8)
        self.rowWidget0Layout.setStretch(2, 2)
        self.rowWidget0Layout.setStretch(3, 1)
        self.rowWidget0.setLayout(self.rowWidget0Layout)

    def createRowWidget1(self):
        self.rowWidget1 = QWidget(self)
        self.rowWidget1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.rowWidget1Layout = QHBoxLayout(self.rowWidget1)
        self.rowWidget1Layout.setSpacing(0)

        slash1 = QLabel(self.rowWidget1)
        slash1.setText("/")
        slash1.setFont(self._font.font24B)
        slash1.setStyleSheet("color: white; border: transparent; padding: 3px;")
        slash1.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        slash2 = QLabel(self.rowWidget1)
        slash2.setText("/")
        slash2.setFont(self._font.font24B)
        slash2.setStyleSheet("color: white; border: transparent; padding: 3px;")
        slash2.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        slash3 = QLabel(self.rowWidget1)
        slash3.setText("-")
        slash3.setFont(self._font.font24B)
        slash3.setStyleSheet("color: white; border: transparent; padding: 10px;")
        slash3.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        slash4 = QLabel(self.rowWidget1)    
        slash4.setText(":")
        slash4.setFont(self._font.font24B)
        slash4.setStyleSheet("color: white; border: transparent; padding: 3px;")
        slash4.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        self.yearLineEdit = QLineEdit(self.rowWidget1)
        self.yearLineEdit.setFont(self._font.font14B)
        self.yearLineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px;")
        self.yearLineEdit.setPlaceholderText("YYYY")
        self.yearLineEdit.setFixedSize(100, 50)
        self.yearLineEdit.setAlignment(Qt.AlignCenter)

        self.monthLineEdit = QLineEdit(self.rowWidget1)
        self.monthLineEdit.setFont(self._font.font14B)
        self.monthLineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px;")
        self.monthLineEdit.setPlaceholderText("MM")
        self.monthLineEdit.setFixedSize(50, 50)
        self.monthLineEdit.setAlignment(Qt.AlignCenter)

        self.dayLineEdit = QLineEdit(self.rowWidget1)
        self.dayLineEdit.setFont(self._font.font14B)
        self.dayLineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px;")
        self.dayLineEdit.setPlaceholderText("DD")
        self.dayLineEdit.setFixedSize(50, 50)
        self.dayLineEdit.setAlignment(Qt.AlignCenter)

        self.hourLineEdit = QLineEdit(self.rowWidget1)
        self.hourLineEdit.setFont(self._font.font14B)
        self.hourLineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px;")
        self.hourLineEdit.setPlaceholderText("hh")
        self.hourLineEdit.setFixedSize(50, 50)
        self.hourLineEdit.setAlignment(Qt.AlignCenter)

        self.minuteLineEdit = QLineEdit(self.rowWidget1)
        self.minuteLineEdit.setFont(self._font.font14B)
        self.minuteLineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px;")
        self.minuteLineEdit.setPlaceholderText("mm")
        self.minuteLineEdit.setFixedSize(50, 50)
        self.minuteLineEdit.setAlignment(Qt.AlignCenter)

        self.typeTrancComboBox = QComboBox(self.rowWidget1)
        self.typeTrancComboBox.setFont(self._font.font14B)
        self.typeTrancComboBox.setStyleSheet("""QComboBox{ background-color: rgba(255, 255, 255, 0.95); color: #575757; padding-left: 10px; padding-bottom: 5px; padding-top: 5px; border: transparent;}
                                            QComboBox:QAbstractItemView{ background-color: rgba(255, 255, 255, 0.95); color: #575757; padding-bottom: 5px; padding-top: 5px; color:orange; padding-left: 10px}""")
        self.typeTrancComboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.typeTrancComboBox.setFixedHeight(50)
        for k in TRANCS_TAG.keys():
            self.typeTrancComboBox.addItem(k)

        self.methodTrancComboBox = QComboBox(self.rowWidget1)
        self.methodTrancComboBox.setFont(self._font.font14B)
        self.methodTrancComboBox.setStyleSheet("""QComboBox{ background-color: rgba(255, 255, 255, 0.95); color: #575757; padding-left: 10px; padding-bottom: 5px; padding-top: 5px; border: transparent;}
                                            QComboBox:QAbstractItemView{ background-color: rgba(255, 255, 255, 0.95); color: #575757; padding-bottom: 5px; padding-top: 5px; color:orange; padding-left: 10px}""")
        self.methodTrancComboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.methodTrancComboBox.setFixedHeight(50)
        for k in PAYMENT_METHOD:
            self.methodTrancComboBox.addItem(k)

        self.rowWidget1Layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget1Layout.addWidget(self.yearLineEdit)
        self.rowWidget1Layout.addWidget(slash1)
        self.rowWidget1Layout.addWidget(self.monthLineEdit)
        self.rowWidget1Layout.addWidget(slash2)
        self.rowWidget1Layout.addWidget(self.dayLineEdit)
        self.rowWidget1Layout.addWidget(slash3)
        self.rowWidget1Layout.addWidget(self.hourLineEdit)
        self.rowWidget1Layout.addWidget(slash4)
        self.rowWidget1Layout.addWidget(self.minuteLineEdit)
        self.rowWidget1Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget1Layout.addWidget(self.typeTrancComboBox)
        self.rowWidget1Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget1Layout.addWidget(self.methodTrancComboBox)
        self.rowWidget1Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget1Layout.setStretch(0, 1)
        self.rowWidget1Layout.setStretch(10, 2)
        self.rowWidget1Layout.setStretch(11, 7)
        self.rowWidget1Layout.setStretch(12, 1)
        self.rowWidget1Layout.setStretch(13, 7)
        self.rowWidget1Layout.setStretch(14, 1)
        self.rowWidget1.setLayout(self.rowWidget1Layout)

    def createRowWidget2(self):
        self.rowWidget2 = QWidget(self)
        self.rowWidget2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.rowWidget2Layout = QHBoxLayout(self.rowWidget2)

        self.addButton = QPushButton(self.rowWidget2)
        self.addButton.setText("Add")
        self.addButton.clicked.connect(self.addButtonHandle)
        self.addButton.setFont(self._font.font20B)
        self.addButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.addButton.setStyleSheet("""QPushButton{ background-color: #e89b27; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                        QPushButton::pressed{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }
                                        QPushButton::hover{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }""")

        self.cancelButton = QPushButton(self.rowWidget2)
        self.cancelButton.setText("Cancel")
        self.cancelButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.cancelButton.clicked.connect(self.cancelButtonHandle)
        self.cancelButton.setFont(self._font.font20B)
        self.cancelButton.setStyleSheet("""QPushButton{ background-color: #e89b27; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                            QPushButton::pressed{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }
                                            QPushButton::hover{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }""")

        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.addWidget(self.addButton)
        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.addWidget(self.cancelButton)
        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.setStretch(0, 3)
        self.rowWidget2Layout.setStretch(1, 2)
        self.rowWidget2Layout.setStretch(2, 3)
        self.rowWidget2Layout.setStretch(3, 2)
        self.rowWidget2Layout.setStretch(4, 3)
        self.rowWidget2.setLayout(self.rowWidget2Layout)

    def addButtonHandle(self):
        if self.trancTitle.text()=="":
            self.message.show("Name of transaction is empty")
        elif self.amount.text()=="":
            self.message.show("Cost is empty")
        else:
            year = int(self.yearLineEdit.text())
            month = int(self.monthLineEdit.text())
            day = int(self.dayLineEdit.text())
            hour = int(self.hourLineEdit.text())
            minute = int(self.minuteLineEdit.text())
            try:
                self.conn.insertRowTransactions(_time=datetime(year=year, month=month, day=day, hour=hour, minute=minute).timestamp(),
                                                title=self.trancTitle.text(),
                                                paymentMethod=self.methodTrancComboBox.currentText(),
                                                trancTag=self.typeTrancComboBox.currentText(),
                                                amount=int(self.amount.text()))
                self.signals.signal_addNewTranc.emit()
                self.close()
            except ValueError:
                self.message.show("Invalid datetime")
            except TypeError:
                self.message.show("Invalid value")

    def cancelButtonHandle(self):
        self.close()

    def requestShow(self, signals):
        self.trancTitle.setText(signals["title"])
        self.amount.setText("")
        self.yearLineEdit.setText(str(signals["now"].year))
        self.monthLineEdit.setText(str(signals["now"].month))
        self.dayLineEdit.setText(str(signals["now"].day))
        self.hourLineEdit.setText(str(signals["now"].hour))
        self.minuteLineEdit.setText(str(signals["now"].minute))
        self.exec_()

    def _closeDialogEvent(self, event):
        pass

class AddShoppingItemDialogSignals(QObject):
    signal_addNewItem = pyqtSignal(str)

class AddShoppingItemDialog(QDialog):
    def __init__(self, app, conn, _font):
        super(AddShoppingItemDialog, self).__init__()
        self.conn = conn
        self._font = _font
        self.setStyleSheet("""QDialog { 
                background-image: url(image/contour-lines-cyan-dark-blue.jpg);
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 40;
            }""")
        self.setWindowTitle("MyApp!")
        self.setGeometry(QStyle.alignedRect(\
                            Qt.LeftToRight,
                            Qt.AlignCenter,
                            QSize(app.primaryScreen().availableGeometry().width()//3,   
                                    app.primaryScreen().availableGeometry().height()//3),
                        app.desktop().availableGeometry()));
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint);
        self.signals = AddShoppingItemDialogSignals()
        self.widgetDialogLayout = QVBoxLayout(self)

        self.dialogTitle = QLabel(self)
        self.dialogTitle.setFont(self._font.font20B)
        self.dialogTitle.setAlignment(Qt.AlignCenter)
        self.dialogTitle.setText("New shopping item")
        self.dialogTitle.setStyleSheet("background-color: transparent; color: #f0f0f0;")
        self.dialogTitle.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.createRowWidget0()
        self.createRowWidget2()

        self.widgetDialogLayout.addWidget(self.dialogTitle)
        self.widgetDialogLayout.addWidget(self.rowWidget0)
        self.widgetDialogLayout.addWidget(self.rowWidget2)
        
        self.setLayout(self.widgetDialogLayout)

    def createRowWidget0(self):
        self.rowWidget0 = QWidget(self)
        self.rowWidget0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.rowWidget0Layout = QHBoxLayout(self.rowWidget0)
        self.rowWidget0Layout.setSpacing(5)

        self.shoppingItemTitle = QLineEdit(self.rowWidget0)
        self.shoppingItemTitle.setFont(self._font.font16B)
        self.shoppingItemTitle.setStyleSheet("background-color: rgba(255, 255, 255, 0.95); color: #575757; border: 3px solid white; border-radius: 10px; padding: 15px;")
        self.shoppingItemTitle.setPlaceholderText("Shopping item title")
        self.shoppingItemTitle.setAlignment(Qt.AlignCenter)
        
        self.rowWidget0Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget0Layout.addWidget(self.shoppingItemTitle)
        self.rowWidget0Layout.addItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget0Layout.setStretch(0, 1)
        self.rowWidget0Layout.setStretch(1, 8)
        self.rowWidget0Layout.setStretch(2, 1)
        self.rowWidget0.setLayout(self.rowWidget0Layout)

    def createRowWidget2(self):
        self.rowWidget2 = QWidget(self)
        self.rowWidget2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.rowWidget2Layout = QHBoxLayout(self.rowWidget2)

        self.addButton = QPushButton(self.rowWidget2)
        self.addButton.setText("Add")
        self.addButton.clicked.connect(self.addButtonHandle)
        self.addButton.setFont(self._font.font20B)
        self.addButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.addButton.setStyleSheet("""QPushButton{ background-color: #e89b27; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                        QPushButton::pressed{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }
                                        QPushButton::hover{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }""")

        self.cancelButton = QPushButton(self.rowWidget2)
        self.cancelButton.setText("Cancel")
        self.cancelButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.cancelButton.clicked.connect(self.cancelButtonHandle)
        self.cancelButton.setFont(self._font.font20B)
        self.cancelButton.setStyleSheet("""QPushButton{ background-color: #e89b27; color: #ffffff; border: transparent; padding: 5; border-radius: 10; }
                                            QPushButton::pressed{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }
                                            QPushButton::hover{ background-color: #ffb274; color: #fffdfa; border: #fffdfa solid 3px; padding: 5; border-radius: 10; }""")

        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.addWidget(self.addButton)
        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.addWidget(self.cancelButton)
        self.rowWidget2Layout.addItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)) # w:20 h:10
        self.rowWidget2Layout.setStretch(0, 3)
        self.rowWidget2Layout.setStretch(1, 2)
        self.rowWidget2Layout.setStretch(2, 3)
        self.rowWidget2Layout.setStretch(3, 2)
        self.rowWidget2Layout.setStretch(4, 3)
        self.rowWidget2.setLayout(self.rowWidget2Layout)

    def addButtonHandle(self):
        self.signals.signal_addNewItem.emit(self.shoppingItemTitle.text())
        self.close()

    def cancelButtonHandle(self):
        self.close()

    def show(self):
        self.shoppingItemTitle.setText("")
        self.exec_()

    def _closeDialogEvent(self, event):
        pass


# """ ========= AppWindow ========= """
class AppWindowSignals(QObject):
    signal = pyqtSignal()

class AppWindow(QMainWindow):
    def __init__(self, app, conn):
        super(AppWindow, self).__init__()
        screen = app.primaryScreen()
        self.conn = conn
        self._font = MFont()
        rect = screen.availableGeometry()
        self.title = "Ứng dụng quản lý chi tiêu"
        self.l = 0
        if OS.startswith("win"):
            self.t = 30
        elif OS.startswith("linux"):
            self.t = 0
        elif OS.startswith("darwin"):
            self.t = 0
        else:
            sys.exit(1)
        self.w = rect.width()
        self.h = rect.height() - self.t
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint);
        self.setWindowFlags(Qt.Window);
        self.addDialog = AddDialog(app, conn, self._font)
        self.addShoppingItemDialog = AddShoppingItemDialog(app, self.conn, self._font)
        self.initUI()
        self.closeEvent = self._closeEvent

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.l, self.t, self.w, self.h)
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

        self.login("Minh Nguyen Thi", "maminhhh", "image/avatar.png")
        self.addDialog.signals.signal_addNewTranc.connect(lambda: self.allExpensesWidget.onActivated(self.allExpensesWidget.durationComboBox.currentText()))
        self.addShoppingItemDialog.signals.signal_addNewItem.connect(lambda title: self.shopTodayWidget.addNew(title))

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
            self.tabButtonList.append(tabButton)

        self.tabBarWidgetLayout.addItem(QSpacerItem(15, 10, QSizePolicy.Expanding, QSizePolicy.Expanding)) # Vertical Space
        settingButton = QPushButton(self.tabBarWidget)
        settingButton.setText("❀")
        settingButton.setFont(self._font.font24)
        settingButton.setStyleSheet("background-color: rgba(206, 217, 220, 0.0); color: #7a7c93; border: transparent; padding: 0; border-radius: 0;")
        self.tabBarWidgetLayout.addWidget(settingButton)
        self.usernameLabel = QLabel(self.tabBarWidget)
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
        self.allExpensesWidget.onActivated("this month")
        self.allExpensesWidget.durationComboBox.setCurrentText("this month")

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

        self.accountWidget = AccountWidget(QWidget(tabWidget), self.addDialog, self._font, self.conn)
        # self.accountWidget.signals.signal_prevAccount.connect()
        # self.accountWidget.signals.signal_nextAccount.connect()
        self.accountWidget.signals.signal_gotoDetailTab.connect(partial(self.onChangeTab, 1))
        self.accountWidget.signals.signal_gotoCardTab.connect(partial(self.onChangeTab, 2))

        self.shopTodayWidget = ShopTodayWidget(QWidget(tabWidget), self.addDialog, self.addShoppingItemDialog, self._font, self.conn)

        self.latestTrancWidget = LatestTrancWidget(QWidget(tabWidget), self.addDialog, self._font, self.conn)
        self.latestTrancWidget.signals.signal_gotoDetailTab.connect(partial(self.onChangeTab, 1))

        self.allExpensesWidget = AllExpensesWidget(QWidget(tabWidget), self.addDialog, self._font, self.conn)
        self.allExpensesWidget.signals.signal_gotoDetailTab.connect(partial(self.onChangeTab, 1))
        self.allExpensesWidget.signals.signal_updateInfoAll.connect(self.reloadMyAccountTab)

        tabWidgetRow0Layout.addWidget(self.accountWidget.accountWidget)
        tabWidgetRow0Layout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum)) # w:15 h:15
        tabWidgetRow0Layout.addWidget(self.shopTodayWidget.shopTodayWidget)
        tabWidgetRow0Layout.setStretch(0, 30)
        tabWidgetRow0Layout.setStretch(1, 1)
        tabWidgetRow0Layout.setStretch(2, 20)
        tabWidgetRow0.setLayout(tabWidgetRow0Layout)

        tabWidgetRow1Layout.addWidget(self.latestTrancWidget.latestTrancWidget)
        tabWidgetRow1Layout.addItem(QSpacerItem(15, 15, QSizePolicy.Maximum, QSizePolicy.Maximum)) # w:15 h:15
        tabWidgetRow1Layout.addWidget(self.allExpensesWidget.allExpensesWidget)
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

    def login(self, username, username_short, avatar):
        self.accountWidget.accountTitleLabel.setText(username)
        self.avatarLabel.setPixmap(QPixmap(avatar).scaled(self.avatarLabel.width(), self.avatarLabel.height(), Qt.KeepAspectRatio, Qt.FastTransformation))
        self.usernameLabel.setText(username_short)

    def reloadMyAccountTab(self, signals):
        self.accountWidget.reload(signals)
        self.latestTrancWidget.reload(signals)
        self.allExpensesWidget.reload(signals)


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





