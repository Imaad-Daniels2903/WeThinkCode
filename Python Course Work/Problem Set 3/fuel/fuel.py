
def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fraction_list = fraction.split("/")
            fractions = [int(char) for char in fraction_list]

            if fractions[0] < 0 or fractions[0] > fractions[1]:
                raise ValueError()

        except ValueError:
            pass

        else:
            try:
                answer = round(fractions[0] / fractions[1], 2)

            except ZeroDivisionError:
                pass

            else:
                percentage = round(answer * 100)
                if percentage == 100 or percentage + 1 == 100:
                    print("F")
                    break

                elif percentage == 0 or percentage - 1 == 0:
                    print("E")
                    break

                else:
                    print(f"{percentage}%")
                    break


if __name__ == "__main__":
    main()
