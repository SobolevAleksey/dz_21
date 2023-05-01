from exceptions import RequestError, LogisticError
from shop_class import Shop
from store_class import Store
from request_class import Request

store = Store(
    items={
        "яблоко": 2,
        "груша": 3,
        "печеньки": 1,
        "слива": 3
    }
)

shop = Shop(
    items={
        "яблоко": 1,
        "груша": 3,
        "печеньки": 2,
        "слива": 1
    }
)

storages = {
    "магазин": shop,
    "склад": store
}

def main():
    print('Доброго времени суток')
    while True:
        # Выводим все товары во всех хранилищах
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        # Делаем запрос у пользователя
        user_input = input("Ввведите запрос в формате 'Доставить 3 печеньки из склад в магазин'\n"
                           "Если хотите закончить введите 'stop' или 'стоп'")

        if user_input in ["стоп", "stop"]:
            break
        try:
            request = Request(storages=storages, request=user_input)
            print(request)
        except RequestError as error:
            print(error.message)
            continue

        # Забираем товар
        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} со {request.departure}')
        except LogisticError as error:
            print(error.message)
            continue

        # Доставляем товар
        try:
            storages[request.destination].add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
        except LogisticError as error:
            print(error.message)
            # Если ошибка на месте получения, то возвращаем товар
            storages[request.departure].add(request.product, request.amount)
            print(f'Курьер вернул {request.amount} {request.product} в {request.departure}')
            continue


if __name__ == "__main__":
    main()