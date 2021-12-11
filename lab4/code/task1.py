from __future__ import annotations
from abc import ABC, abstractmethod
#абстракная фабрика

class AbstractFactory(ABC):

    @abstractmethod
    def create_book(self) -> AbstractBook:
        pass

    @abstractmethod
    def create_section(self) -> AbstractSection:
        pass


class Pushkin(AbstractFactory):

    def create_book(self) -> AbstractBook:
        return PushkinBook()

    def create_section(self) -> AbstractSection:
        return PushkinSection()


class Lermontov(AbstractFactory):

    def create_book(self) -> AbstractBook:
        return LermontovBook()

    def create_section(self) -> AbstractSection:
        return LermontovSection()


class AbstractBook(ABC):

    @abstractmethod
    def read_the_book(self) -> str:
        pass


class PushkinBook(AbstractBook):
    def __init__(self, name='Dubrovsky'):
        self.name=name
    def read_the_book(self) -> str:
        return f"The book named <<{self.name}>>"

class LermontovBook(AbstractBook):
    def __init__(self, name='Borodino'):
        self.name=name
    def read_the_book(self) -> str:
        return f"The book named <<{self.name}>>"


class AbstractSection(ABC):
    @abstractmethod
    def tell_the_section_name(self) -> None:
        pass

    @abstractmethod
    def find_a_book_in_the_section(self, collaborator: AbstractBook) -> None:
        pass


class PushkinSection(AbstractSection):
    def tell_the_section_name(self) -> str:
        return "The Pushkin's section."

    def find_a_book_in_the_section(self, collaborator: AbstractBook) -> str:
        result = collaborator.read_the_book()
        return f"{result} from Pushkin's section"

class LermontovSection(AbstractSection):
    def tell_the_section_name(self) -> str:
        return "The Lermontov's section."

    def find_a_book_in_the_section(self, collaborator: AbstractBook) -> str:
        result = collaborator.read_the_book()
        return f"{result} from Lermontov's section"



def client_code(factory: AbstractFactory) -> None:
    book=factory.create_book()
    section=factory.create_section()
    print(f"{section.find_a_book_in_the_section(book)}")

if __name__ == "__main__":

    print("Вася прочитал сегодня:")
    client_code(Pushkin())

    print("Саша прочитала сегодня:")
    client_code(Lermontov())