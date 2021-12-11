import unittest
from tasks import *
from generators import *

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.builds = builds_generator()
        self.streets = steets_generator()
        build_placing({
            0: [0,1],
            2: [2,4,3],
            4: [5,6,7],
            5: [10, 9, 8]
                            }, self.streets, self.builds)
        self.crosses = street_crossing([
    [0, 1], [0, 0], [2, 2], [2, 4], [2, 3], [4, 5], [4, 6], [4, 7], [5, 10], [5, 9], [5, 8],
    [3, 0], [1, 10], [1, 8]
])

    def test_taskA1(self):
        compareWith=[('Ленинский пр-кт', 483, 13), ('Ленинский пр-кт', 484, 18), ('Ленинский пр-кт', 485, 11),
                     ('Молдавский пр-кт', 1, 14), ('Молдавский пр-кт', 14, 28), ('Петра Великого', 13, 103),
                     ('Петра Великого', 15, 238), ('Петра Великого', 14, 89), ('Серебряная', 15, 45),
                     ('Серебряная', 16, 44), ('Серебряная', 17, 56)]
        self.assertEqual(taskA1(one_to_many_generator(self.streets, self.builds)), compareWith)

    def test_taskA2(self):
        compareWith=[('Петра Великого', 430), ('Серебряная', 145), ('Ленинский пр-кт', 42), ('Молдавский пр-кт', 42)]
        self.assertEqual(taskA2(one_to_many_generator(self.streets, self.builds)), compareWith)

    def test_taskA3(self):
        compareWith={'Молдавский пр-кт': [1, 14], 'Житомирский пр-кт': [1], 'Ленинский пр-кт': [483, 484, 485]}
        self.assertEqual(taskA3(many_to_many_generator(self.streets, self.builds, self.crosses)), compareWith)

if __name__ == '__main__':
    unittest.main()
