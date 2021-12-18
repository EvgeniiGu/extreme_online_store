from FlaskWebProject1.OrdersSetsList import OrdersSetsList
from FlaskWebProject1.OrdersList import OrdersList
from FlaskWebProject1.EmployeesList import EmployeesList


class Dispatcher():
    def __init__(self, id):
        self.__id = id
        OrdersSetsList.download_from_file()
        OrdersList.download_from_file()
        EmployeesList.download_from_file()

    @staticmethod
    def get_list_of_sets():
        list = OrdersSetsList.get_list()
        return [(list[i].id, list[i].orders_id_list, list[i].status, list[i].id_of_the_courier_who_delivers)
                for i in range(len(list))]

    @staticmethod
    def create_set(data):
        OrdersSetsList.add_new_ordersset(*data)
        OrdersSetsList.download_to_file()

    @staticmethod
    def get_list_of_orders():
        list = OrdersList.get_list()
        return [(list[i].id, list[i].goods_id_list, list[i].status) for i in range(len(list))]

    @staticmethod
    def delete_set(id):
        list = OrdersSetsList.get_list()
        for i in range(len(list)): list.pop(i) if list[i].id == id else None
        OrdersSetsList.download_to_file()

    @staticmethod
    def get_list_of_couriers():
        list = EmployeesList.get_list()
        list = [[list[i].id, None] for i in range(len(list)) if list[i].position == "Courier "]
        for i in OrdersSetsList.get_list():
            for j in range(len(list)):
                if i.id_of_the_courier_who_delivers == list[j][0]: list[j][1] = i.id
        return list
