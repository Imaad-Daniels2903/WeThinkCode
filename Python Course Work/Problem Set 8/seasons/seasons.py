from datetime import date
import inflect
import sys


def main():
    try:
        print(get_minutes(input("Date of Birth: ")))

    except ValueError:
        sys.exit("Invalid date")


def get_minutes(dob):
    p = inflect.engine()
    user_dob = date.fromisoformat(dob.strip())
    today = date.today()
    total_days = (today - user_dob).days
    total_minutes = total_days * 24 * 60
    return f"{p.number_to_words(total_minutes, andword="")} minutes".capitalize()





if __name__ == "__main__":
    main()
