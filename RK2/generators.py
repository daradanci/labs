from objects import *
import json

def one_to_many_generator(streets: list, builds: list):
    return [(s.name, b.num, b.people)
            for b in builds
            for s in streets
            if b.streetID == s.id]

def many_to_many_generator(streets: list, builds: list, buildstreets: list):
    many_to_many_temp = [(s.name, bs.streetID, bs.buildID)
                         for s in streets
                         for bs in buildstreets
                         if s.id == bs.streetID
                         ]
    return [(s_name, b.num, b.people)
            for s_name, streetID, buildID in many_to_many_temp
            for b in builds if b.id == buildID
            ]

def builds_generator():
    with open('data.json', 'r') as file:
        data = json.load(file)
    builds=[]
    index=0
    for build in data:
        builds.append(Building(index, build["num"], build["people"], build["year"]))
        index = index + 1
    return builds

def steets_generator():
    streets=[]
    index=0
    with open('streets.json', 'r', encoding='utf-8') as file:
        data=json.load(file)
    for streetname in data:
        streets.append(Street(index, streetname))
        index = index + 1
    return streets

# для построения связи один-ко-многим
# {id улицы : [id зданий]}
def build_placing(input: dict, streets: list, builds: list):
    for streetnumb in range(0, len(streets)):
        if streetnumb in input:
            for buildnumb in input[streetnumb]:
                builds[buildnumb].set_street(streetnumb)

# для построения связи многие-ко-многим
# [id улицы, id здания]
def street_crossing(input: list):
    return [BuildStreet(con[0],con[1]) for con in input]
