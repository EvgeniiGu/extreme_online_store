import sqlite3 as sq
from FlaskWebProject1.Order import Order
from FlaskWebProject1.SomeShitTestModule import from_list_to_string_converter


class OrdersList():

    @staticmethod
    def download_from_file():
        OrdersList.__List = []
        with sq.connect("extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM orderslist")
            Shit_list = cur.fetchall()
            for i in range(len(Shit_list)):
                data = (Shit_list[i][0], (Shit_list[i][1]).split(), Shit_list[i][2])
                OrdersList.__List.append(Order(*data))

    @staticmethod
    def download_to_file():
        with sq.connect("extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM orderslist")
            for i in range(len(OrdersList.__List)):
                data = ((OrdersList.__List[i]).id,
                        from_list_to_string_converter((OrdersList.__List[i]).goods_id_list),
                        (OrdersList.__List[i]).status)
                cur.execute("INSERT INTO orderslist VALUES(?,?,?)", (data))

    @staticmethod
    def add_new_order(goods_id_list, status):
        n = [OrdersList.__List[i].id for i in range(len(OrdersList.__List))]
        for id in range(300000, 400000):
            if str(id) not in n:
                OrdersList.__List.append(Order(str(id), goods_id_list, status))
                break

    @staticmethod
    def change_status(id, new_status):
        for i in range(len(OrdersList.__List)):
            if OrdersList.__List[i].id == id:
                OrdersList.__List[i].status = new_status
                break

    @staticmethod
    def delete_order(id):
        for i in range(len(OrdersList.__List)):
            if OrdersList.__List[i].id == id:
                OrdersList.__List.pop(i)
                break

    @staticmethod
    def get_list():
        return OrdersList.__List

    @staticmethod
    def set_list(new_list):
        OrdersList.__List = new_list

