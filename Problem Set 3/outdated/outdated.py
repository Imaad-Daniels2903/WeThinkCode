
MONTHS = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "0: "11",
    "December" : "12"
}

def main():
    while True:
        try:
            date = input("Date: ").strip().title()
            date_list = date.split()
            if not date_list[0] in MONTHS and (len(date_list) > 1 and  not date_list[0].isalpha()):
                raise ValueError()

        except ValueError:
            pass

        else:
            if len(date_list) == 1:
                output_list = []
                output = date_list[0].split("/")
                for x in output:
                    if len(x) == 1:
                        output_list.append(f"0{x}")

                    elif len(x) == 4:
                        output_list.insert(0, x)

                    else:
                        output_list.append(x)
                print("-".join(output_list))
                break

            else:
                output_list = []
                for x in date_list:
                    if x in MONTHS:
                        output_list.append(MONTHS[x])

                    elif len(x) == 1 or len(x) == 2 and "," in x:
                        output_list.append(f"0{x[0]}")

                    elif len(x) == 4:
                        output_list.insert(0, x)

                    else:
                        output_list.append(x)

                print("-".join(output_list))
                break


if __name__ == "__main__":
    main()
