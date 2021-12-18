from dataclasses import dataclass

@dataclass()
class OrdersSet():
    id: str
    orders_id_list: list
    status: str
    id_of_the_courier_who_delivers: str = None
