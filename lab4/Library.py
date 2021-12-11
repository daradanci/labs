from __future__ import annotations
from abc import ABC, abstractmethod

EnglishBookStandartName='Pride & Prejudice'
RussianBookStandartName='Война и мир'
#абстракная фабрика

class AbstractFactory(ABC):
    @abstractmethod
    def create_book(self, name) -> AbstractBook:
        pass
    @abstractmethod
    def create_reader(self) -> AbstractReader:
        pass


class English(AbstractFactory):
    def create_book(self, name=EnglishBookStandartName) -> AbstractBook:
        return EnglishBook(name)

    def create_reader(self) -> AbstractReader:
        return EnglishReader()


class Russian(AbstractFactory):
    def create_book(self, name=RussianBookStandartName) -> AbstractBook:
        return RussianBook(name)

    def create_reader(self) -> AbstractReader:
        return RussianReader()


class AbstractBook(ABC):
    @abstractmethod
    def read(self) -> str:
        pass


class EnglishBook(AbstractBook):
    def __init__(self, name=EnglishBookStandartName):
        self.name=name
    def read(self) -> str:
        return f"The book named <<{self.name}>>"

class RussianBook(AbstractBook):
    def __init__(self, name=RussianBookStandartName):
        self.name=name
    def read(self) -> str:
        return f"Книга под названием <<{self.name}>>"


class AbstractReader(ABC):
    @abstractmethod
    def tell_something(self) -> None:
        pass
    @abstractmethod
    def read_a_book(self, collaborator: AbstractBook) -> None:
        pass


class EnglishReader(AbstractReader):
    def tell_something(self) -> str:
        return "I wanna read something."
    def read_a_book(self, collaborator: AbstractBook) -> str:
        result = collaborator.read()
        if (self.check_language(collaborator)):
            return f"I have read {result} and enjoyed it."
        else:
            return f"I don't understand <<{result}>> and I hate it."

    def check_language(self, book: AbstractBook)->bool:
        return isinstance(book, EnglishBook)


class RussianReader(AbstractReader):
    def tell_something(self) -> str:
        return "Почитать хочется."

    def read_a_book(self, collaborator: AbstractBook) -> str:
        result = collaborator.read()
        if (self.check_language(collaborator)):
            return f"{result} мне очень понравилась!"
        else:
            return f"Я не понимаю <<{result}>>, что за ерунда?"


    def check_language(self, book: AbstractBook)->bool:
        return isinstance(book, RussianBook)

def client_code(factory: AbstractFactory, bookName) -> str:
    book=factory.create_book(bookName)
    reader=factory.create_reader()
    return f"{reader.read_a_book(book)}"
#адаптер
class TranslatorToRussian(RussianBook, EnglishBook):
    def __init__(self, enBook:EnglishBook):
        self.enBook=enBook

    def translate(self)->RussianBook:
        return RussianBook(f"Перевод: {self.enBook.read()} - теперь доступно на русском языке!")


if __name__ == "__main__":

    '''    enbook=EnglishBook('The Old Man and the Sea')
        translator=TranslatorToRussian(enbook)
        rubook=translator.translate()
        print(rubook.name)
        print(client_code(Russian(), rubook.name))'''


