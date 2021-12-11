

class Building:
    def __init__(self, id, num, people, year):
        self.id=id
        self.num=num
        self.people=people
        self.year=year
        self.streetID=-1
    def set_street(self, streetID):
        self.streetID=streetID
    def __str__(self):
        return f" {self.id} {self.num}  {self.people}  {self.year}  {self.streetID}"

class Street:
    def __init__(self, id,name):
        self.id=id
        self.name=name
    def __str__(self):
        return f"{self.id}  {self.name}"

class BuildStreet:
    def __init__(self, streetID, buildID):
        self.streetID=streetID
        self.buildID=buildID
    def __str__(self):
        return f"{self.streetID}  {self.buildID}"