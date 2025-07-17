
from tabulate import tabulate
import sys
import csv

def main():
    csv_filename = sys.argv
    try:
        menu_list ,headers = get_info(csv_filename)

    except FileNotFoundError:
        sys.exit("File does not exit")

    else:
        print(tabulate(menu_list, headers, tablefmt="grid"))


def get_info(csv_filename):
    if len(csv_filename) >= 3:
        sys.exit("Too many command-line arguments")

    elif len(csv_filename) == 1:
        sys.exit("Too few command-line arguments")

    elif not csv_filename[1][-4:] == ".csv":
        sys.exit("Not a CSV file")

    else:
        menu_list = []
        headers = []
        csv_file = csv_filename[1]
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            for line in reader:
                menu_list.append([line[headers[0]], line["Small"], line["Large"]])

            return menu_list, headers




if __name__ == "__main__":
    main()
