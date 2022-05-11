from random import randint
import csv


def generate_data():
    with open('sample_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow([]) # array with column names
        for i in range(1000):
            request_data = []
            insurance_id = i + 1
            request_data.append(insurance_id)
            # condition = CONDITION[randint(0, 2)]
            # request_data.append(condition)
            # country = COUNTRY[randint(0, len(COUNTRY) - 1)]
            # request_data.append(country)
            price = f"{randint(900, 5000)}"
            request_data.append(price)
            is_available = 1
            request_data.append(is_available)
            # title = TITLE[randint(0, 7)]
            # request_data.append(title)
            reserved_by_user = 'none'
            request_data.append(reserved_by_user)
            writer.writerow(request_data)


generate_data()
