def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

        else:
            print(gauge(percentage))


def convert(fraction):
    fraction_list = fraction.split("/")
    x = fraction_list[0]
    y = fraction_list[1]

    if (x.isalpha() or y.isalpha()):
        raise ValueError()

    else:
        if int(y) == 0:
            raise ZeroDivisionError()

        else:
            if int(x) < 0 or int(y) < 0:
                raise ValueError()

            else:
                if int(x) > int(y):
                    raise ValueError()

                else:
                    return round((int(x) / int(y)) * 100)


def gauge(percentage):

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
