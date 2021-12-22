from FlaskWebProject1.SomeShitTestModule import from_list_to_string_converter
from FlaskWebProject1.OrdersSet import OrdersSet
import sqlite3 as sq


class OrdersSetsList():

    @staticmethod
    def download_from_file():
        OrdersSetsList.__List = []
        with sq.connect("FlaskWebProject1/extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS orderssetslist (
                       id TEXT,
                       orders_id_list TEXT,
                       status TEXT,
                       id_of_the_courier_who_delivers TEXT )""")
            cur.execute("SELECT * FROM orderssetslist")
            Shit_list = cur.fetchall()
            for i in range(len(Shit_list)):
                data = [Shit_list[i][0], (Shit_list[i][1]).split(), Shit_list[i][2], Shit_list[i][3]]
                OrdersSetsList.__List.append(OrdersSet(*data))

    @staticmethod
    def download_to_file():
        with sq.connect("extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM orderssetslist")
            for i in range(len(OrdersSetsList.__List)):
                data = (OrdersSetsList.__List[i].id,
                        from_list_to_string_converter(OrdersSetsList.__List[i].orders_id_list),
                        OrdersSetsList.__List[i].status, OrdersSetsList.__List[i].id_of_the_courier_who_delivers)
                cur.execute("INSERT INTO orderssetslist VALUES(?,?,?,?)", data)

    @staticmethod
    def add_new_ordersset(orders_id_list, status, id_of_the_courier_who_delivers):
        n = [OrdersSetsList.__List[i].id for i in range(len(OrdersSetsList.__List))]
        for id in range(400000, 500000):
            if str(id) not in n:
                OrdersSetsList.__List.append(OrdersSet(str(id), orders_id_list, status, id_of_the_courier_who_delivers))
                break

    @staticmethod
    def delete_ordersset(id):

        for i in range(len(OrdersSetsList.__List)):
            if (OrdersSetsList.__List[i]).id == id:
                OrdersSetsList.__List.pop(i)
                break

    @staticmethod
    def get_list():
        return OrdersSetsList.__List

    @staticmethod
    def set_list(new_list):
        OrdersSetsList.__List = new_list

