from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QWidget, QPushButton, QListWidget, QGridLayout
from datetime import datetime
from .utils import *
from .transaction_item import TransactionItem

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
            
