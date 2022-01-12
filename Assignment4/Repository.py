import sqlite3
import atexit
from DAO import _Hats, _Suppliers, _Orders

class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('spl4.db')
        self.hats = _Hats(self._conn)
        self.supplier = _Suppliers(self._conn)
        self.orders = _Orders(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE suppliers (
            id    INTEGER  PRIMARY KEY,
            name  TEXT     NOT NULL
        );
        CREATE TABLE hats (
            id       INTEGER  PRIMARY KEY,
            topping  TEXT     NOT NULL,
            supplier INTEGER  REFERENCES Supplier(id),
            quantity INTEGER  NOT NULL
        );
        CREATE TABLE orders (
            id       INTEGER  PRIMARY KEY,
            location TEXT     NOT NULL,
            hat INTEGER  REFERENCES hats(id)
        );
        """)


repo = _Repository()
atexit.register(repo._close)