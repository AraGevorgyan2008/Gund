import csv
class Person:
    def __init__(self, ID, name, age, pasport, race, place, gender, number,sitting_place):
        self.ID=ID
        self.name = name
        self.age = age
        self.passport = passport
        self.race = race
        self.place = place
        self.gender = gender
        self.number = number
        self.sitting_place = sitting_place
    def __str__(self):
        return f"Name {self.name}\n Age {self.age}\n Passport {self.passport}\n Race {self.race}\n Place {self.place}\n Gender {self.gender}\n Number {self.number}\n Sitting Place {self.sitting_place}"
n=int(input())
people=[]
for i in range(n):
    ID=input()
    name=input()
    age=input()
    passport=input()
    race=input()
    place=input()
    gender=input()
    number=input()
    sitting_place=input()
    p=Person(ID,name, age, passport, race, place, gender, number, sitting_place)
    people.append(p)
with open("data1.csv", "w", newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["ID", "Name", "Age", "Passport", "Race", "Place", "Gender", "Number", "Sitting Place"])
    for i in people:
        writer.writerow([i.ID, i.name, i.age, i.passport, i.race, i.place, i.gender, i.number, i.sitting_place])
def tpel(filename):
    with open(filename, "r") as f:
        r=csv.reader(f)
        for row in r:
            print(f"Name: {row[1]}")
            print(f"Age: {row[2]}")
            print(f"Passport: {row[3]}")
            print(f"Race: {row[4]}")
            print(f"Place: {row[5]}")
            print(f"Gender: {row[6]}")
            print(f"Number: {row[7]}")
            print(f"Sitting Place: {row[8]}")
tpel("data1.csv")