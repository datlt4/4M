import sqlite3

class ConnectDatabase():
    def __init__(self, db_file) -> None:
        try:
            self.conn = sqlite3.connect(db_file)
        except sqlite3.Error as e:
            self.conn = None

        assert self.conn is not None, "sqlite3.Error when create connection to your database"

    def queryRowsShoppingList(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM ShoppingList;")
        row = cur.fetchall()
        return row

    def deleteRowShoppingList(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM ShoppingList WHERE ID = (?);", (id,))
        except BaseException:
            print('activity is incomplete - deleteRowShoppingList')
        finally:
            self.conn.commit()

    def insertRowTransactions(self, _time, title, paymentMethod, trancTag, amount):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO Transactions (trancTime, trancTitle, trancPaymentMethod, trancTag, amount) VALUES ((?), (?), (?), (?), (?))",
                (_time, title, paymentMethod, trancTag, amount))
        except sqlite3.IntegrityError:
            print('activity is incomplete - insertRowTransactions')
        finally:
            self.conn.commit()

    def queryRowsTransactions(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("SELECT * FROM Transactions;")
        elif (_from is not None) and (_to is None):
            cur.execute("SELECT * FROM Transactions WHERE trancTime >= (?);", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("SELECT * FROM Transactions WHERE trancTime <= (?);", (_to,))
        else:
            cur.execute("SELECT * FROM Transactions WHERE trancTime >= (?) AND trancTime <= (?);", (_from, _to))

        row = cur.fetchall()
        return row

    def querySumTransactionInEachTag(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("SELECT trancTag, sum(amount) FROM Transactions GROUP BY trancTag;")
        elif (_from is not None) and (_to is None):
            cur.execute("SELECT trancTag, sum(amount) FROM Transactions WHERE trancTime >= (?) GROUP BY trancTag;", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("SELECT trancTag, sum(amount) FROM Transactions WHERE trancTime <= (?) GROUP BY trancTag;", (_to,))
        else:
            cur.execute("SELECT trancTag, sum(amount) FROM Transactions WHERE trancTime >= (?) AND trancTime <= (?) GROUP BY trancTag;", (_from, _to))

        row = cur.fetchall()
        return row

    def querySumExpensesInEachTag(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag NOT IN ('Salary', 'Other Income');""", )
        elif (_from is not None) and (_to is None):
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                WHERE trancTime >= (?)
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag NOT IN ('Salary', 'Other Income');""", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                WHERE trancTime <= (?)
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag NOT IN ('Salary', 'Other Income');""", (_to,))
        else:
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                WHERE trancTime >= (?)
                                    AND trancTime <= (?)
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag NOT IN ('Salary', 'Other Income');""", (_from, _to))

        row = cur.fetchall()
        return row
