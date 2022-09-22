import storage
import storage_exceptions as s_exc


class Model:
    def __init__(self, start_items: list = None):
        self._item_type = 'еда'
        if start_items is None:
            start_items = []
        self.create_items(start_items)

    @property
    def item_type(self) -> str:
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type: str):
        self._item_type = new_item_type

    @staticmethod
    def create_item(name: str, price: int, quantity: int) -> None:
        storage.create_item(name, price, quantity)

    @staticmethod
    def create_items(items: list) -> None:
        storage.create_items(items)

    @staticmethod
    def read_item(name: str):
        return storage.read_item(name)

    @staticmethod
    def read_items():
        return storage.read_items()

    @staticmethod
    def update_item(name: str, price: int, quantity: int):
        storage.update_item(name, price, quantity)

    @staticmethod
    def delete_item(name: str):
        storage.delete_item(name)


class View:
    @staticmethod
    def show_bullet_point_list(item_type: str, items: list):
        print(f'—————————— {item_type.upper()} СПИСОК ——————————')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type: str, items: list):
        print(f'—————————— {item_type.upper()} СПИСОК ——————————')
        for i, item in enumerate(items):
            print(f'{i+1}. {item}')

    @staticmethod
    def show_item(item_type: str, item_name: str, item_info: dict):
        print('//////////////////////////////////////////////////////////////')
        print(f'У нас есть {item_name.upper()}!')
        print(f'{item_type} информация: {item_info}')
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def show_missing_item_error(item_name: str, error_message: str):
        print('**************************************************************')
        print(f'У нас нет {item_name.upper()}!')
        print(f'{error_message}')
        print('**************************************************************')

    @staticmethod
    def show_item_already_stored_error(item_name: str, item_type: str, error_message: str):
        print('**************************************************************')
        print(f'У нас уже есть {item_name.upper()} в списке {item_type.upper()}!')
        print(f'{error_message}')
        print('**************************************************************')

    @staticmethod
    def show_item_stored(item_name: str, item_type: str):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'Ура! Мы добавили {item_name.upper()} в список {item_type.upper()}!')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def show_item_updated(item_name: str,
                          old_price: int,
                          old_quantity: int,
                          new_price: int,
                          new_quantity: int):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Изменение цены {item_name}: {old_price} --> {new_price}')
        print(f'Изменение количества {item_name}: {old_quantity} --> {new_quantity}')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def show_item_deleted(item_name: str, item_type: str):
        print('--------------------------------------------------------------')
        print(f'Мы убрали {item_name.upper()} из списка {item_type.upper()}!')
        print('--------------------------------------------------------------')


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def show_item(self, item_name: str):
        try:
            item = self.model.read_item(item_name)
            self.view.show_item(
                self.model.item_type,
                item_name,
                item
            )
        except s_exc.ItemNotStoredError as e:
            self.view.show_missing_item_error(item_name, str(e))

    def show_items(self, bullets: bool = False):
        items = self.model.read_items()
        if bullets:
            self.view.show_bullet_point_list(
                self.model.item_type,
                items
            )
        else:
            self.view.show_number_point_list(
                self.model.item_type,
                items
            )

    def insert_item(self, name: str, price: int, quantity: int):
        try:
            self.model.create_item(name, price, quantity)
            self.view.show_item_stored(
                name,
                self.model.item_type
            )
        except s_exc.ItemAlreadyStoredError as e:
            self.view.show_item_already_stored_error(
                name,
                self.model.item_type,
                str(e)
            )

    def update_item(self, name: str, price: int, quantity: int):
        try:
            old = self.model.read_item(name)
            self.model.update_item(name, price, quantity)
            self.view.show_item_updated(
                name,
                old['price'], old['quantity'],
                price, quantity
            )
        except s_exc.ItemNotStoredError as e:
            self.view.show_missing_item_error(name, str(e))

    def delete_item(self, name: str):
        try:
            self.model.delete_item(name)
            self.view.show_item_deleted(
                name,
                self.model.item_type
            )
        except s_exc.ItemNotStoredError as e:
            self.view.show_missing_item_error(name, str(e))



grossery_store = Controller(Model(), View())
print()
grossery_store.insert_item('молоко', 85, 20)
print()
grossery_store.insert_item('квас', 55, 30)
print()
grossery_store.insert_item('вино', 450, 10)
print()
grossery_store.show_items()














