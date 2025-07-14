
import inflect
import sys

def main():
    name_list = []
    while True:

        try:
            name = input("Name: ").strip().title()

        except EOFError:
            p = inflect.engine()
            print(f"Adieu, adieu, to {p.join(name_list)}")
            sys.exit()

        else:
            name_list.append(name)



if __name__ == "__main__":
    main()
