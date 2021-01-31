from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QLabel, QSizePolicy, QWidget, QGridLayout, QListWidgetItem
from PyQt5.QtGui import QFont
from .utils import *

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
