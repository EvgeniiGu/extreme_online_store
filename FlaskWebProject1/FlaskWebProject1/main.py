from Good import Good
from Employee import Employee
from EmployeesList import EmployeesList
from GoodsList import GoodsList
from OrdersList import OrdersList
from Order import Order
from OrdersSet import OrdersSet
from OrdersSetsList import OrdersSetsList
from Storekeeper import Storekeeper
from Dispatcher import Dispatcher
from Courier import Courier

#EmployeesList.download_from_file()
#EmployeesList.delete_worker(100001)
#EmployeesList.add_new_worker("Иaaaван", "nnn", 23, "fff", "uuu", "uuu")
#print(EmployeesList.get_list()[0].id)
#EmployeesList.download_to_file()

#GoodsList.download_from_file()
#GoodsList.add_new_good(456.78, "Красный шар", "14")
#GoodsList.delete_good("200000")
#GoodsList.download_to_file()

#OrdersList.download_from_file()
#OrdersList.delete_order(300006)
#OrdersList.add_new_order([200004, 200005], "returned")
#OrdersList.download_to_file()

#OrdersSetsList.download_from_file()
#OrdersSetsList.delete_ordersset(400001)
#OrdersSetsList.add_new_ordersset([300001], "processed", None)
#OrdersSetsList.download_to_file()

#Test1 = Storekeeper("100000")
#print(Test1.get_list_of_orders())
#Test1.save_list_of_orders([('300001', ['200001', '200004'], 'проёбан'), ('300000', ['200001', '200002'], 'assembled')])
#Test1.save_list_of_products([('200001', '456.78', 'Красный шар', '15'), ('200002', '123.40', 'Синий шар', '3'), ('200003', '79', 'Зелёный шар', '57'), ('200004', '99.99', 'Белый шар', '45')])
#Test2 = Dispatcher("100001")
#print(Test2.get_list_of_couriers())

Test3 = Courier("100003")
Test3.take_set("400000")
Test3.deliver_order()