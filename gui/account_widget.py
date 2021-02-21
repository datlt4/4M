from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSpacerItem, QWidget, QPushButton, QGridLayout, QSizePolicy
from .utils import *
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

