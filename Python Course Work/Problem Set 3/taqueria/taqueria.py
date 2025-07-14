
MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while True:
        try:
            input_item = input("Item: ").strip().title()
            amount_due = MENU[input_item]

        except EOFError:
            print("\n", end="")
            break

        except KeyError:
            pass

        except ValueError:
            break

        else:
            total += amount_due
            print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
