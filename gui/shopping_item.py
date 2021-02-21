from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QLabel, QSpacerItem, QSizePolicy, QListWidgetItem, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from .utils import *

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
