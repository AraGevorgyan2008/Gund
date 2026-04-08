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
print(p)
with open("Persons.txt","w") as f:
    f.write(str(p))