import sqlite3 as sq
from FlaskWebProject1.Good import Good


class GoodsList():

    @staticmethod
    def download_from_file():
        GoodsList.__List = []
        with sq.connect("FlaskWebProject1/extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS goodslist (
            id TEXT,
            cost TEXT,
            title TEXT,
            quantity_in_stock TEXT )""")
            cur.execute("SELECT * FROM goodslist")
            Shit_list = cur.fetchall()

            for i in range(len(Shit_list)):
                GoodsList.__List.append(Good(*Shit_list[i]))

    @staticmethod
    def download_to_file():
        with sq.connect("extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM goodslist")
            for i in range(len(GoodsList.__List)):
                data = ((GoodsList.__List[i]).id, (GoodsList.__List[i]).cost,
                        (GoodsList.__List[i]).title, (GoodsList.__List[i]).quantity_in_stock)
                cur.execute("INSERT INTO goodslist VALUES(?,?,?,?)", (data))

    @staticmethod
    def add_new_good(cost, title, quantity_in_stock):
        n = [GoodsList.__List[i].id for i in range(len(GoodsList.__List))]
        for id in range(200000, 300000):
            if str(id) not in n:
                GoodsList.__List.append(Good(str(id), cost, title, quantity_in_stock))
                break

    @staticmethod
    def change_quantity_in_stock(id, new_quantity_in_stock):
        for i in range(len(GoodsList.__List)):
            if GoodsList.__List[i].id == id:
                GoodsList.__List[i].quantity_in_stock = new_quantity_in_stock
                break

    @staticmethod
    def delete_good(id):
        for i in range(len(GoodsList.__List)):
            if GoodsList.__List[i].id == id:
                GoodsList.__List.pop(i)
                break

    @staticmethod
    def get_list():
        return GoodsList.__List

    @staticmethod
    def set_list(new_list):
        GoodsList.__List = new_list
