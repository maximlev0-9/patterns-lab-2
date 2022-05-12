from random import randint
import csv

first_names = [
    "Maria",
    "Nushi",
    "Mohammed",
    "Jose",
    "Muhammad",
    "Mohamed",
    "Wei",
    "Mohammad",
    "Ahmed",
    "Yan",
    "Ali",
    "John",
    "David",
    "Li",
    "Abdul",
    "Ana",
    "Ying",
    "Michael",
    "Juan",
    "Anna",
    "Mary",
    "Jean",
    "Robert",
    "Daniel",
    "Luis",
    "Carlos",
    "James",
    "Antonio",
    "Joseph",
    "Hui",
    "Elena",
    "Francisco",
    "Hong",
    "Marie",
    "Min",
    "Lei",
    "Yu",
    "Ibrahim",
    "Peter",
    "Fatima",
    "Aleksandr",
    "Richard",
    "Xin",
    "Bin",
    "Paul",
    "Ping",
    "Lin",
    "Olga",
    "Sri",
    "Pedro",
    "William",
    "Rosa",
    "Thomas",
    "Jorge",
    "Yong",
    "Elizabeth",
    "Sergey",
    "Ram",
    "Patricia",
    "Hassan",
    "Anita",
    "Manuel",
    "Victor",
    "Sandra",
    "Ming",
    "Siti",
    "Miguel",
    "Emmanuel",
    "Samuel",
    "Ling",
    "Charles",
]
last_names = [
    "SMITH",
    "JOHNSON",
    "WILLIAMS",
    "BROWN",
    "JONES",
    "GARCIA",
    "MILLER",
    "DAVIS",
    "RODRIGUEZ",
    "MARTINEZ",
    "HERNANDEZ",
    "LOPEZ",
    "GONZALEZ",
    "WILSON",
    "ANDERSON",
    "THOMAS",
    "TAYLOR",
    "MOORE",
    "JACKSON",
    "MARTIN",
    "LEE",
    "PEREZ",
    "THOMPSON",
    "WHITE",
    "HARRIS",
    "SANCHEZ",
    "CLARK",
]

def generate_data():
    with open("random_data.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["id", "name", "phone_number", "email"]
        )  # array with column names
        for i in range(1000):
            request_data = []
            insurance_id = i + 1
            request_data.append(insurance_id)
            first_name = first_names[randint(0, len(first_names)-1)]
            last_name = last_names[randint(0, len(last_names)-1)].lower().capitalize()
            name = first_name + " " + last_name
            request_data.append(name)
            phone_number = f"+380{randint(0, 360_000_000) + 640_000_000}"
            request_data.append(phone_number)
            email = (first_name[:3] + last_name + "@gmail.com").lower()
            request_data.append(email)
            writer.writerow(request_data)

generate_data()
