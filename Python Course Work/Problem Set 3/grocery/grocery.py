
def main():
    grocery_list = {}
    while True:
        try:
            item = input()

        except EOFError:
            print("\n", end="")
            break

        else:
            if item in grocery_list:
                grocery_list[item] += 1

            else:
                grocery_list[item] = 1

    final_list = dict(sorted(grocery_list.items()))
    for key  in final_list:
        print(f"{final_list[key]} {key.upper()}")


if __name__ == "__main__":
    main()
