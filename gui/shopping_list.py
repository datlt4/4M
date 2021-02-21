from functools import partial
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QWidget, QPushButton, QListWidget, QGridLayout
from PyQt5.QtGui import QPixmap
from datetime import datetime
from .utils import *
from .shopping_item import ShoppingItem 


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

