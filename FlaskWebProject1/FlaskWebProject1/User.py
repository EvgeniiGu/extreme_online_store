from FlaskWebProject1.Admin import Admin
from FlaskWebProject1.EmployeesList import EmployeesList


class User:
    position_ = ["Courier", "Dispatcher", "Storekeeper"]
    def recognize(self, login, password):
        if Admin.is_admin(login, password):
            return "Admin"
        else:
            EmployeesList.download_from_file()
            employees_list = EmployeesList.get_list()
            for j in range(len(employees_list)):
                if employees_list[j].login == login and employees_list[j].password == password:
                    return employees_list[j].position
                else:
                    return -1
