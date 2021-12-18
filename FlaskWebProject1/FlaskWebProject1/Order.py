from dataclasses import dataclass

@dataclass()
class Order():
    id: str
    goods_id_list: list
    status: str