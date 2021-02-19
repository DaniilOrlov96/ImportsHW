from datetime import datetime

from Application.salary import *
from db.people import *

if __name__ == '__main__':
    calculate_salary()
    date = datetime.today()
    print('now ', date)

if __name__ == '__main__':
    get_employees()
    date = datetime.today()
    print('now ', date)

