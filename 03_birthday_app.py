import datetime


def print_header():
    print("----------------------")
    print("  BIRTHDAY")
    print("----------------------")
    print()


def get_birthday_from_user():
    print("Tell us when you were born: ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))
    birthday = datetime.datetime(year, month, day)
    return birthday

def compute_days_between_dates():
    pass

def print_birthday_info():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = None
    #umber_of_days = compute_days_between_dates(bday, now)
    #print_birthday_info(number_of_days)

main()