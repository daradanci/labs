from Library import *
from unittest import TestCase
from unittest.mock import patch

class TestLibrary(TestCase):

    @patch('Library.client_code', side_effect=[
        "Книга под названием <<Анна Каренина>> мне очень понравилась!",
        "I have read The book named <<Tom Sawyer>> and enjoyed it.",

    ])
    def test_client_code(self, ccode):
        self.assertEqual(ccode(Russian(), 'Анна Каренина'),
                     "Книга под названием <<Анна Каренина>> мне очень понравилась!")
        self.assertEqual(ccode(English(), 'Tom Sawyer'),
                     "I have read The book named <<Tom Sawyer>> and enjoyed it.")

    @patch('Library.client_code', side_effect=TypeError)
    def test_error_cc(self, ccode):
        self.assertRaises(TypeError,(Russian()))

    @patch.object(RussianReader(),'read_a_book', side_effect=[
        "I have read The book named <<Romeo and Juliet>> and enjoyed it.",
        # "Книга под названием <<Руслан и Людмила>> мне очень понравилась!",
        # "I don't understand <<Книга под названием <<Руслан и Людмила>>>> and I hate it.",
        # "Я не понимаю <<The book named <<Romeo and Juliet>>>>, что за ерунда?"

    ])
    def test_readers_with_books(self, rbook, side_effect):
        self.assertEqual(rbook(RussianBook("Romeo and Juliet")), side_effect[0])