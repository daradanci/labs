import unittest
from Library import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Olga=RussianReader()
        self.John=EnglishReader()
        self.ruBook=RussianBook('Руслан и Людмила')
        self.enBook=EnglishBook('Romeo and Juliet')
    def test_client_code(self):
        result=client_code(Russian(), 'Анна Каренина')
        self.assertEqual(result, "Книга под названием <<Анна Каренина>> мне очень понравилась!")
        result=client_code(English(), 'Tom Sawyer')
        self.assertEqual(result, "I have read The book named <<Tom Sawyer>> and enjoyed it.")

    def test_client_code_without_a_book_name(self):
        with self.assertRaises(TypeError):
            client_code(Russian())

    def test_acceptable_books(self):
        self.assertEqual(self.Olga.read_a_book(self.ruBook),
                         "Книга под названием <<Руслан и Людмила>> мне очень понравилась!")
        self.assertEqual(self.John.read_a_book(self.enBook),
                         "I have read The book named <<Romeo and Juliet>> and enjoyed it.")

    def test_unacceptable_books(self):
        self.assertEqual(self.Olga.read_a_book(self.enBook),
                         "Я не понимаю <<The book named <<Romeo and Juliet>>>>, что за ерунда?")
        self.assertEqual(self.John.read_a_book(self.ruBook),
                         "I don't understand <<Книга под названием <<Руслан и Людмила>>>> and I hate it.")

    def test_standart_names(self):
        self.assertEqual(RussianBook().name, RussianBookStandartName)
        self.assertEqual(EnglishBook().name, EnglishBookStandartName)

    def test_translator_to_Russian(self):
        self.assertEqual(TranslatorToRussian(self.enBook).translate().name,
                         "Перевод: The book named <<Romeo and Juliet>> - теперь доступно на русском языке!")
    def test_client_code_with_translator(self):
        rubook=TranslatorToRussian(self.enBook).translate()
        self.assertEqual(client_code(Russian(), rubook.name),
                         "Книга под названием <<Перевод: The book named <<Romeo and Juliet>> - теперь доступно на русском языке!>> мне очень понравилась!")

    def test_English_reader_with_wrong_translation(self):
        enbook=TranslatorToRussian(self.enBook).translate()
        self.assertEqual(self.John.read_a_book(enbook),
                         "I don't understand <<Книга под названием <<Перевод: The book named <<Romeo and Juliet>> - теперь доступно на русском языке!>>>> and I hate it.")

if __name__ == '__main__':
    unittest.main()
