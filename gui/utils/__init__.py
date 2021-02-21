import sys

OS = sys.platform
username = "Minh Nguyen"
avatar = "image/avatar.png"
PAYMENT_METHOD = ["Other Method", "VN Pay", "Card Payment", "Fee", "Cash", "Momo", "Airpay", "Zalo Pay", "Transfer", "Grab by Moca"]
INCOME_TAG = {"Salary": "#277a44", "Other Income": "#72d6c2"}
EXPENSE_TAG = {"Other": "#51546f", "Food": "#b1d672", "Bills": "#7963cd", "Entertainment": "#ff8f78", "Health": "#c13c3c", "Education": "#3dbce0", "Clothes": "#cbb64d"}
TRANCS_TAG = dict(item for _dict in [EXPENSE_TAG, INCOME_TAG] for item in _dict.items())
MONTH = {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"}

OS = sys.platform
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

