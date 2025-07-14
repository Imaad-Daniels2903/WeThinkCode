
def subtract(coke_amount, amount):
    coke_amount -= amount

    if coke_amount < 0:
        print(f"Change owed: {coke_amount * -1}")

    elif coke_amount == 0:
        print(f"Change owed: {coke_amount}")

    else:
        print(f"Amount due: {coke_amount}")

    return coke_amount


def main():
    coke_amount = 50
    while coke_amount > 0:

        inserted_amount = input("Insert coin: ")

        match inserted_amount:
            case "25" :
                coke_amount = subtract(coke_amount, 25)

            case "10" :
                coke_amount = subtract(coke_amount, 10)

            case "5" :
                coke_amount = subtract(coke_amount, 5)

            case _ :
                print(f"Amount due: {coke_amount}")



if __name__ == "__main__":
    main()
