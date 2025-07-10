def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >= 2 and s.isalnum():
        if s[0:2].isalpha() and s[-2:].isdigit():
            num_cnt = 0
            for x in s:
                if x.isdigit():
                    num_cnt += 1
                    if num_cnt == 1 and x == "0":
                        return False
                        break
                    else:
                        return True
                        break
                else:
                    continue
        elif s.isalpha():
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
