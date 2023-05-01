class BaseError(Exception):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class NotEnoughSpace(LogisticError):
    message = "Недостаточно места"


class NotEnoughProduct(LogisticError):
    message = "Недостаточно продукта"


class TooMuch(LogisticError):
    message = "Слишком много товара"
class UnknowProduct(LogisticError):
    message = "Нет такого товара"


class InvalidRequest(RequestError):
    message = "Неправильный запрос. Попробуй снова"


class InvalidStorageName(RequestError):
    message = "Неправильный запрос. Нет такого хранилища"
