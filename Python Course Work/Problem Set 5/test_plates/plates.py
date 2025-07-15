def main():
    user_input = input("Plate: ").strip()
    if is_valid(user_input):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0:2].isalpha():
            if s.isalpha():
                return True

            elif s.isalnum():
                if s[-2:].isdigit():
                    digit_count = 0
                    for char in s:
                        if char.isdigit():
                            digit_count += 1
                            if not (char == "0" and digit_count == 1):
                                return True
                            else:
                                return False
                        else:
                            continue
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
