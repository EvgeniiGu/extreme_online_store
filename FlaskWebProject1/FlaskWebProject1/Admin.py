from FlaskWebProject1.EmployeesList import EmployeesList
from FlaskWebProject1.GoodsList import GoodsList

class Admin:
    __LOGIN = "1"
    __PASSWORD = "1"

    @staticmethod
    def is_admin(login, password):
        return login == Admin.__LOGIN and password == Admin.__PASSWORD

    def get_list_employees(self):
        EmployeesList.download_from_file()
        employees_list = EmployeesList.get_list()
        len_employees_list = len(employees_list)
        new_employees_list = list()
        for j in range(len_employees_list):
            new_employees_list.append(employees_list[j].name)
            new_employees_list.append(employees_list[j].surname)
            new_employees_list.append(employees_list[j].age)
            new_employees_list.append(employees_list[j].position)
            new_employees_list.append(employees_list[j].login)
            new_employees_list.append(employees_list[j].password)
        iter_list_employees_ = [it for it in range(len(new_employees_list))]
        new_employees_list_shell = {"iter_list_employees_": iter_list_employees_, "workers": new_employees_list}
        return new_employees_list_shell
    def get_list_goods(self):
        GoodsList.download_from_file()
        goods_list = GoodsList.get_list()
        len_goods_list = len(goods_list)
        new_goods_list = list()    
        iter_goods_list_ = [it for it in range(len_goods_list)]
        for f in range(len_goods_list):
            new_goods_list.append(goods_list[f].title)
            new_goods_list.append(goods_list[f].cost)
            new_goods_list.append(goods_list[f].quantity_in_stock)
        new_goods_list_shell = {"iter_goods_list_": iter_goods_list_, "goods": new_goods_list}
        return new_goods_list_shell
    def save_new_list_employees(self, list):
        pass
    def save_new_list_products(self, list):
        pass
    def create_new_category():
        pass

    def delete_category():
        pass

    def create_employee():
        pass

    def delete_employee():
        pass