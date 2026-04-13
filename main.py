import csv

class Aviacompany:
    def __init__(self, ID, name, number):
        self.ID = ID
        self.name = name
        self.number = number

    def __str__(self):
        return f"Aviacompany[ID={self.ID}, Name={self.name}, Number={self.number}]"

    def get_info(self):
        return {
            "Id": self.ID,
            "Name": self.name,
            "Number": self.number
        }

    def update_name(self, new_name):
        self.name = new_name

    def update_number(self, new_number):
        self.number = new_number

    def add(self, filename="aviacompany.csv"):
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.ID, self.name, self.number])
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
def findAv(Id):
    with open('aviacompany.csv', "r") as file1:
        r = file1.readlines()
        for i in r:
            if i[0].isdigit():
                if int(i[0]) == Id:
                    return  i



a = Person(1,"fdf",25,"12599755","A3333",1,"dfwe",947568555,"5A")
print(findAv(1))
