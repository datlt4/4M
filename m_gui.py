import sys
from functools import partial
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QApplication, QSizePolicy, QWidget, QPushButton, QGridLayout, QStackedWidget
from PyQt5.QtGui import QPixmap
from gui import *

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





