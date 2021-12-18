def check_int(x):#1
    if isinstance(x, int):
        return x
    else:
        raise ValueError("Неверный формат данных, ожидался int")
    
def check_str(x):#2
    if isinstance(x, str):
        return x
    else:
        raise ValueError("Неверный формат данных, ожидался str")


def check_float(x):#3
    if isinstance(x, float):
        return x
    else:
        raise ValueError("Неверный формат данных, ожидался float")


def check_list(x):#4
    if isinstance(x, list):
        return x
    else:
        raise ValueError("Неверный формат данных, ожидался list")
#1-4 зачем?????
#

def check_id(id, tipe):#что за tipe?///  id генерится автоматически, зачем его проверять???????
    if tipe == "Employee":#в чем проблема использовать должность? У нас специально это поле в классе есть
        if len(str(id)) == 6 and str(id)[0] == "1":
            return id
        else:
            raise ValueError("Неверный формат данных, проверь id")

    if tipe == "Good":
        if len(str(id)) == 6 and str(id)[0] == "2":
            return id
        else:
            raise ValueError("Неверный формат данных, проверь id")

    if tipe == "Order":
        if len(str(id)) == 6 and str(id)[0] == "3":
            return id
        else:
            raise ValueError("Неверный формат данных, проверь id")

    if tipe == "Set":
        if len(str(id)) == 6 and str(id)[0] == "4":
            return id
        else:
            raise ValueError("Неверный формат данных, проверь id")
    raise ValueError("Неверный формат данных, проверь id")#ты же в курсе, что в таком случае он всегда ошибку высрет???

def from_list_to_string_converter(List):# а это что?зачем? почему это в тестовом модуле?
    string = ""
    for i in range(len(List)):
        string += str(List[i])
        string += " "
    return string[:len(string)-1]
#Говно, переделывай