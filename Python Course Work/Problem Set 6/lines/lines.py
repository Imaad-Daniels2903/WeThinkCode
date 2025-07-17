
import sys

def main():
    filename = sys.argv
    print(filename)
    try:
        line_count = count_lines(filename)

    except FileNotFoundError:
        sys.exit("File does not exist")

    else:
        print(line_count)

def count_lines(filename):
    if len(filename) >= 3:
        sys.exit("Too many command-line arguments")

    elif len(filename) == 1:
        sys.exit("Too few command-line arguments")

    elif not filename[1][-3:] == ".py":
        sys.exit("Not a python file")

    else:
        python_file = filename[1]
        with open(python_file, "r") as file:
            line_count = 0
            for line in file:
                if len(line.strip()) > 0 and line.strip()[0] == "#":
                    ...

                elif line.strip() == "":
                    ...

                else:
                    line_count += 1

            return line_count

if __name__ == "__main__":
    main()

