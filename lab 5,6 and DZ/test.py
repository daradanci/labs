import unittest
#from admin import message_about_deletion
from handlers.admin import message_about_deletion
from handlers.client import message_about_buying
from handlers.other import just_answerer

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.painting_name='Jolyne Cujoh'
    def test_message_about_deletion(self):
        self.assertEqual(message_about_deletion(self.painting_name), f'"{self.painting_name}" has been deleted.')
        #self.assertEqual(True, True)
    def test_message_about_buying(self):
        self.assertEqual(message_about_buying(self.painting_name), f'You have bought "{self.painting_name}".')
    def test_simple_answers(self):
        self.assertEqual(just_answerer('Hello!'), 'Hello there! How are you?')
        self.assertEqual(just_answerer('I am fine, thanks!'), 'What a nice day to see you here!')
        self.assertEqual(just_answerer('You too!'), ':^)')
if __name__ == '__main__':
    unittest.main()
