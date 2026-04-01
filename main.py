import csv

class Person:
    def __init__(self, name, age, pasport, race, place, gender, number,sitting_place):
        self.name = name
        self.age = age
        self.pasport = pasport
        self.race = race
        self.place = place
        self.gender = gender
        self.number = number
        self.sitting_place = sitting_place

    def add(self):
        with open('data.csv', "a") as csvfile:
            w = csv.writer(csvfile)
            w.writerow([self.race, self.place, self.gender, self.number, self.sitting_place])
