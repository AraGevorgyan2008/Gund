import csv

class Person:
    def __init__(self, ID, name, age, passport, race, place, gender, number,sitting_place):
        self.ID=ID
        self.name = name
        self.age = age
        self.passport = passport
        self.race = race
        self.place = place
        self.gender = gender
        self.number = number
        self.sitting_place = sitting_place

    def add(self):
        with open('data1.csv', "a") as csvfile:
            w = csv.writer(csvfile)
            w.writerow([self.ID,self.name,self.age,self.passport,self.race, self.place, self.gender, self.number, self.sitting_place])

    def __str__(self):
        return f"Name {self.name}\n Age {self.age}\n Passport {self.passport}\n Race {self.race}\n Place {self.place}\n Gender {self.gender}\n Number {self.number}\n Sitting Place {self.sitting_place}"

    def change(self):
        with open('data1.csv', "r") as f:
            data = f.readlines()
            for i in data:


a = Person(1,"fdf",25,"12599755","A3333","ddefdew","dfwe",947568555,"5A")
a.add()
a.change()
