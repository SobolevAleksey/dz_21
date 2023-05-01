from exceptions import InvalidStorageName


class Request():
    """ Разбиваем запрос по атрибутам. Проверяем существуют ли такие хранилища"""
    def __init__(self, storages, request):
        self.storages = storages
        data = request.lower().split(' ')
        if len(data) != 7:
            # raise InvalidRequest
            pass
        self.departure = data[4]
        self.destination = data[6]
        self.amount = int(data[1])
        self.product = data[2]

        if self.departure not in storages and self.destination not in storages:
            raise InvalidStorageName
