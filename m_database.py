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

    def insertRowShoppingList(self, title):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO ShoppingList (itemTitle) VALUES (?)",
                (title,))
        except sqlite3.IntegrityError:
            print('activity is incomplete - insertRowTransactions')
        finally:
            self.conn.commit()
        
        cur = self.conn.cursor()
        cur.execute("SELECT seq FROM sqlite_sequence WHERE name='ShoppingList'")
        row = cur.fetchone()[0]
        return row

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
        
        cur = self.conn.cursor()
        cur.execute("SELECT seq FROM sqlite_sequence WHERE name='Transactions'")
        row = cur.fetchone()[0]
        return row

    def queryRowsTransactions(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("SELECT * FROM Transactions ORDER BY trancTime ASC;")
        elif (_from is not None) and (_to is None):
            cur.execute("SELECT * FROM Transactions WHERE trancTime >= (?) ORDER BY trancTime ASC;", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("SELECT * FROM Transactions WHERE trancTime <= (?) ORDER BY trancTime ASC;", (_to,))
        else:
            cur.execute("SELECT * FROM Transactions WHERE (trancTime >= (?) AND trancTime <= (?)) ORDER BY trancTime ASC;", (_from, _to))

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
        return row if row else [("Other", 0)]

    def querySumExpenses(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE trancTag NOT IN ('Salary', 'Other Income');""", )
        elif (_from is not None) and (_to is None):
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE (trancTag NOT IN ('Salary', 'Other Income'))
                                AND (trancTime >= (?));""", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE (trancTag NOT IN ('Salary', 'Other Income'))
                                AND (trancTime <= (?));""", (_to,))
        else:
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE (trancTag NOT IN ('Salary', 'Other Income'))
                                AND (trancTime >= (?))
                                AND (trancTime <= (?));""", (_from, _to))
        row = cur.fetchone()[0]
        return 0 if row is None else row

    def querySumIncomeInEachTag(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag IN ('Salary', 'Other Income');""", )
        elif (_from is not None) and (_to is None):
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                WHERE trancTime >= (?)
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag IN ('Salary', 'Other Income');""", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                WHERE trancTime <= (?)
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag IN ('Salary', 'Other Income');""", (_to,))
        else:
            cur.execute("""SELECT * 
                            FROM
                                (SELECT trancTag, sum(amount) AS sum
                                FROM Transactions
                                WHERE trancTime >= (?)
                                    AND trancTime <= (?)
                                GROUP BY trancTag) AS E
                            WHERE E.trancTag IN ('Salary', 'Other Income');""", (_from, _to))

        row = cur.fetchall()
        return row if row else [("Other Income", 0)]

    def querySumIncome(self, _from=None, _to=None):
        cur = self.conn.cursor()
        if (_from is None) and (_to is None):
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE trancTag IN ('Salary', 'Other Income');""", )
        elif (_from is not None) and (_to is None):
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE (trancTag IN ('Salary', 'Other Income'))
                                AND (trancTime >= (?));""", (_from,))
        elif (_from is None) and (_to is not None):
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE (trancTag IN ('Salary', 'Other Income'))
                                AND (trancTime <= (?));""", (_to,))
        else:
            cur.execute("""SELECT sum(amount) AS sum
                            FROM Transactions
                            WHERE (trancTag IN ('Salary', 'Other Income'))
                                AND (trancTime >= (?))
                                AND (trancTime <= (?));""", (_from, _to))

        row = cur.fetchone()[0]
        return 0 if row is None else row

    def queryMinTransactionTime(self):
        cur = self.conn.cursor()
        cur.execute("SELECT min(trancTime) FROM Transactions;")
        row = cur.fetchone()
        return row[0]


