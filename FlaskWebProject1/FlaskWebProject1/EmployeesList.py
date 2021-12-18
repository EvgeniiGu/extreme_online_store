import sqlite3 as sq
from FlaskWebProject1.Employee import Employee


class EmployeesList():

    @staticmethod
    def download_from_file():
        EmployeesList.__List = []
        with sq.connect("FlaskWebProject1/extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM employeeslist")
            Shit_list = cur.fetchall()
            for i in range(len(Shit_list)):
                EmployeesList.__List.append(Employee(*Shit_list[i]))

    @staticmethod
    def download_to_file():
        with sq.connect("extreme_store.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM employeeslist")
            for i in range(len(EmployeesList.__List)):
                data = ((EmployeesList.__List[i]).id, (EmployeesList.__List[i]).name,
                        (EmployeesList.__List[i]).surname, (EmployeesList.__List[i]).age,
                        (EmployeesList.__List[i]).login, (EmployeesList.__List[i]).password,
                        (EmployeesList.__List[i]).position)
                cur.execute("INSERT INTO employeeslist VALUES(?,?,?,?,?,?,?)", (data))

    @staticmethod
    def add_new_worker(name, surname, age, login, password, position):
        n = [EmployeesList.__List[i].id for i in range(len(EmployeesList.__List))]
        for id in range(100000, 200000):
            if str(id) not in n:
                (EmployeesList.__List).append(Employee(str(id), name, surname, age, login, password, position))
                break

    @staticmethod
    def delete_worker(id):
        for i in range(len(EmployeesList.__List)):
            if EmployeesList.__List[i].id == id:
                EmployeesList.__List.pop(i)
                break

    @staticmethod
    def get_list():
        return EmployeesList.__List

# код ниже создаёт таблицу, использовать один раз, если таблица будет удалена
# cur.execute("""CREATE TABLE IF NOT EXISTS employeeslist (
# id INTEGER,
# name TEXT,
# surname TEXT,
# age INTEGER,
# login TEXT,
# password TEXT,
# position TEXT
# )""")
