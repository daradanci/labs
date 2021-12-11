#адаптер
class RussianBook:
    def read(self)->str:
        return "Книга на русском языке"


class EnglishBook:
    def try_to_read(self)->str:
        return "The book in English"


class Translator(RussianBook, EnglishBook):
    def read(self)->str:
        return f"Перевод: {self.try_to_read()} - теперь доступно на русском языке!"

def client_code(book: "RussianBook") -> None:
    print(book.read(), end='')

if __name__ == "__main__":
    print("Клиент: Я умею читать только книги на русском языке:")
    rubook=RussianBook()
    client_code(rubook)
    print("\n")


    enbook=EnglishBook()
    print("Клиент: Я не понимаю английский!")
    print(f'EnglishBook: {enbook.try_to_read()}', end='\n\n')


    print('Клиент: Прошу перевод!')
    translator=Translator()
    client_code(translator)
