from DTO import Hat, Supplier, Order


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
               INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ? , ? , ?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def find(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM hats WHERE id = ?
        """, [hat_id])
        return Hat(*c.fetchone())

    def min(self,_topping):
        c = self._conn.cursor()
        c.execute("""SELECT supplier FROM hats WHERE topping = ? 
                """,[_topping,])
        return c.fetchone();

    def deleteZero(self):
        self._conn.execute(""" DELETE FROM hats WHERE  quantity = 0""")

    def update(self, minSupplier ,topping):
        c = self._conn.cursor()
        c.execute(""" UPDATE hats  SET quantity = quantity - 1 WHERE  supplier = ?
        AND topping = ?
   """ , [minSupplier ,topping])

class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
               INSERT INTO suppliers (id, name) VALUES (?, ?)
           """, [supplier.id, supplier.name])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM suppliers WHERE id = ?
        """, [supplier_id])
        return Supplier(*c.fetchone())


class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
               INSERT INTO orders (id, location, hat) VALUES (?, ? , ?)
           """, [order.id, order.location, order.hat])

    def find(self, order_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM orders WHERE id = ?
        """, [order_id])
        return Order(*c.fetchone())
