import random


def main():
    level = get_level()
    count = 0
    score = 0
    while count < 10:
        x, y = generate_integer(level), generate_integer(level)
        wrong = 0
        count += 1
        answer = x + y
        while True:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == answer:
                score += 1
                break
            else:
                wrong += 1
                print("EEE")
                if wrong == 3:
                    wrong = 0
                    print(f"{x} + {y} = {answer}")
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ").strip()
        if not level.isdigit() or int(level) <= 0 or int(level) > 3:
            pass

        else:
            break

    return int(level)


def generate_integer(level):

    match level:
        case 1:
            output = random.randint(0, 9)
            return output

        case 2:
            output = random.randint(10, 99)
            return output

        case 3:
            output = random.randint(100, 999)
            return output

        case _:
            return None


if __name__ == "__main__":
    main()
