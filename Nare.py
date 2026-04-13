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

    def save_to_csv(self, filename="aviacompany.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Number"])
            writer.writerow([self.ID, self.name, self.number])
