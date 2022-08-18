import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

print(datetime.date.today())

if __name__ == '__main__':
    get_employees()
    calculate_salary()

