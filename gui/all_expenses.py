from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QComboBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QSizePolicy, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from datetime import datetime, timedelta
from .utils import *

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

