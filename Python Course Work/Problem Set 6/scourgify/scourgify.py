import csv
import sys

def main():
    csv_filenames = sys.argv
    try:
        format(csv_filenames)

    except FileNotFoundError:
        sys.exit(f"Could not read {csv_filenames[1]}")



def format(csv_filenames):
    if len(csv_filenames) >= 4:
        sys.exit("Too many command-line arguments")

    elif len(csv_filenames) <= 2:
        sys.exit("Too few command-line arguments")

    elif not csv_filenames[1][-4:] == ".csv":
        sys.exit("Not a CSV file")

    else:
        old_file, new_file = csv_filenames[1:]
        with open(old_file, "r") as old, open(new_file, "w") as new:
            reader = csv.DictReader(old)
            writer = csv.DictWriter(new, fieldnames=["first", "last", "house"] )
            writer.writeheader()
            for line in reader:
                last, first = line["name"].split(",")
                writer.writerow(
                    {
                        "first" : first.strip(),
                        "last" : last.strip(),
                        "house" : line["house"].strip()
                    }
                )


if __name__ == "__main__":
    main()
