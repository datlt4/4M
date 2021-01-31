from .utils import *
from PyQt5.QtGui import QFont

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
