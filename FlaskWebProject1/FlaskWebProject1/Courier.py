from FlaskWebProject1.OrdersSetsList import OrdersSetsList
from FlaskWebProject1.OrdersSet import OrdersSet
class Courier:
    def __init__(self):
        #self.__id = id
        self.__set_in_delivery = None
        OrdersSetsList.download_from_file()
        #for i in OrdersSetsList.get_list():
        #    print
        #    if i.id == self.__id: self.__set_in_delivery = i.id_of_the_courier_who_delivers

    @staticmethod
    def get_list_of_sets():
        list = OrdersSetsList.get_list()
        return [(list[i].id, list[i].orders_id_list, list[i].status, list[i].id_of_the_courier_who_delivers)
                for i in range(len(list))]

    def take_set(self, id):
        for i in OrdersSetsList.get_list():
            if i.id == id:
                OrdersSetsList.set_list([j for j in OrdersSetsList.get_list() if j.id != id]
                                        + [OrdersSet(i.id, i.orders_id_list, "in_delivery" , self.__id)])
                self.__set_in_delivery = i.id
                break
        OrdersSetsList.download_to_file()

    def deliver_order(self):
        for i in OrdersSetsList.get_list():
            print(i.id, self.__set_in_delivery)
            if i.id == self.__set_in_delivery:
                OrdersSetsList.set_list([j for j in OrdersSetsList.get_list() if j.id != self.__set_in_delivery]
                                        + [OrdersSet(i.id, i.orders_id_list, "delivered", None)])
                print(OrdersSetsList.get_list())
                self.__set_in_delivery = None
                OrdersSetsList.download_to_file()
                break

