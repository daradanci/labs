from objects import *
from operator import itemgetter
from generators import *
from tasks import *

builds=builds_generator()
streets=steets_generator()

for street in streets:
    print(street, end='   ')
print('\n')
for build in builds:
    print(build, end="  ")
print('\n\n')


build_placing({
    0: [0,1],
    2: [2,4,3],
    4: [5,6,7],
    5: [10, 9, 8]
}, streets, builds)

for build in builds:
    print(build, end="  ")
print('\n\n')

print("Задание А1")
print(taskA1(one_to_many_generator(streets, builds)))
print("Задание А2")
print(taskA2(one_to_many_generator(streets, builds)))

crosses = street_crossing([
    [0, 1], [0, 0], [2, 2], [2, 4], [2, 3], [4, 5], [4, 6], [4, 7], [5, 10], [5, 9], [5, 8],
    [3, 0], [1, 10], [1, 8]
])
print("Задание А3")
print(taskA3(many_to_many_generator(streets, builds, crosses)))
