from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from datetime import date

#очередь

class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового класса
    обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Возврат обработчика отсюда позволит связать обработчики простым
        # способом, вот так:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""



class BookPurityChecker(AbstractHandler):
    def handle(self, request: dict) -> str:
        if request.get('purity')<5:
            return f'Книга "{request.get("name")}" испорчена! Штраф 3200р!'
        else:
            return super().handle(request)
        
class BookPagesChecker(AbstractHandler):
    def handle(self, request: dict) -> str:
        if request.get('actual pages')<request.get('pages'):
            return f'Книга "{request.get("name")}" испорчена! Не хватает {-request.get("actual pages")+request.get("pages")} страниц. Штраф 2500р!'
        else:
            return super().handle(request)
        
class BookDateChecker(AbstractHandler):
    def handle(self, request: dict) -> str:
        if date.today()> request.get('date of hand over'):
            return f'Книга "{request.get("name")}" просрочена! Штраф 4200р! \n ' \
                   f'Сдать нужно было {request.get("date of hand over")}'
        else:
            return super().handle(request)


def client_code(handler: Handler, bookData: dict) -> None:
    result=handler.handle(bookData)
    if (result):
        print(result)
    else:
        print(f'Книга "{bookData.get("name")}" успешно сдана!')

if __name__ == "__main__":

    pages=BookPagesChecker()
    purity=BookPurityChecker()
    hdate=BookDateChecker()

    pages.set_next(purity).set_next(hdate)
    # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
    # только первому в цепочке.

    bookData1 = {
        'name': "Мастер и Маргарита", 'date of hand over': date(2021, 10, 13),
        'pages': 415, 'actual pages': 412, 'purity': 7
    }
    bookData2 = {
        'name': "Яся", 'date of hand over': date(2021, 11, 13),
        'pages': 104, 'actual pages': 104, 'purity': 9
    }

    print("Chain: pages > purity > date")
    client_code(pages, bookData1)
    client_code(pages, bookData2)
    print("\n")

    print("Subchain: purity > date")
    client_code(purity, bookData1)
    client_code(purity, bookData2)