from pprint import pprint

import storage_exceptions as s_exc

items = []

# CRUD — Create, Read, Update, Delete
# стандартный набор операций манипуляции с данными — низкоуровневые функции, зависящие от реализации хранилища — используются высокоуровневой Моделью
def create_item(name: str, price: int, quantity: int) -> None:
    global items
    existing = tuple(filter(
        lambda item: item['name'] == name,
        items
    ))
    if existing:
        raise s_exc.ItemAlreadyStoredError(f'{name} уже сохранён!')
    else:
        items.append(
            {'name': name, 'price': price, 'quantity': quantity}
        )

def create_items(items_list: list[dict]) -> None:
    global items
    items = items_list


def read_item(name: str) -> dict:
    global items
    found = tuple(filter(
        lambda item: item['name'] == name,
        items
    ))
    if found:
        return found[0]
    else:
        raise s_exc.ItemNotStoredError(f'Невозможно извлечь {name}, так как запись отсутствует.')

def read_items() -> list[dict]:
    global items
    return [item for item in items]


def update_item(name: str, price: int, quantity: int) -> None:
    global items
    indexed_items = tuple(filter(
        lambda ind_item: ind_item[1]['name'] == name,
        enumerate(items)
    ))
    if indexed_items:
        items[indexed_items[0][0]] = {
            'name': name, 'price': price, 'quantity': quantity
        }
    else:
        raise s_exc.ItemNotStoredError(f'Невозможно обновить {name}, так как запись отсутствует.')


def delete_item(name: str) -> None:
    global items
    indexed_items = tuple(filter(
        lambda ind_item: ind_item[1]['name'] == name,
        enumerate(items)
    ))
    if indexed_items:
        del items[indexed_items[0][0]]
    else:
        raise s_exc.ItemNotStoredError(f'Невозможно удалить {name}, так как запись отсутствует.')


if __name__ == '__main__':
    test_items = [
        {'name': 'хлеб', 'price': 35, 'quantity': 20},
        {'name': 'молоко', 'price': 85, 'quantity': 10},
        {'name': 'вино', 'price': 500, 'quantity': 5},
    ]
    create_items(test_items)
    pprint(read_items())
    print()

    # print(read_item('шоколад'))
    print(read_item('молоко'), end='\n\n')

    # update_item('рыба', 700, 2)
    update_item('хлеб', 35, 17)
    print(read_item('хлеб'), end='\n\n')

    create_item('шоколад', 150, 6)
    pprint(read_items())
