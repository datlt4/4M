from PyQt5.QtCore import Qt, QObject, pyqtSignal, QSize
from PyQt5.QtWidgets import QComboBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QWidget, QPushButton, QDialog, QStyle
from datetime import datetime
from .utils import *

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
        self.message = Message(app, self._font)
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
        if self.shoppingItemTitle.text()=="":
            self.message.show("Name of shopping item is empty")
        else:    
            self.signals.signal_addNewItem.emit(self.shoppingItemTitle.text())
            self.close()

    def cancelButtonHandle(self):
        self.close()

    def show(self):
        self.shoppingItemTitle.setText("")
        self.exec_()

    def _closeDialogEvent(self, event):
        pass
