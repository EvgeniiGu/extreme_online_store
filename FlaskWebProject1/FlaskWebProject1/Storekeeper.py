from FlaskWebProject1.OrdersList import OrdersList
from FlaskWebProject1.GoodsList import GoodsList
from FlaskWebProject1.Good import Good
from FlaskWebProject1.Order import Order

class Storekeeper():
    def __init__(self):
        GoodsList.download_from_file()
        OrdersList.download_from_file()
       # self.__id = id

    @staticmethod
    def get_list_of_orders():
        list = OrdersList.get_list()
        return [(list[i].id, list[i].goods_id_list, list[i].status)
                for i in range(len(list)) if ((list[i]).status == "created" or list[i]).status == "returned"]

    @staticmethod
    def get_list_of_products():
        list = GoodsList.get_list()
        return [(list[i].id, list[i].cost, list[i].title, list[i].quantity_in_stock) for i in range(len(list))]

    @staticmethod
    def save_list_of_orders(new_list_of_orders):
        list = OrdersList.get_list()
        OrdersList.set_list([list[i] for i in range(len(list)) if not (list[i]).status == "created"] +
                            [Order(*data) for data in new_list_of_orders])
        OrdersList.download_to_file()

    @staticmethod
    def save_list_of_products (list_of_tuples_of_changes):
        GoodsList.set_list([Good(*data) for data in list_of_tuples_of_changes])
        GoodsList.download_to_file()
