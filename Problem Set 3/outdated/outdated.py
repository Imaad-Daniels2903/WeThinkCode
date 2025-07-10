
MONTHS = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

def main():
    while True:
        try:
            date = input("Date: ").strip().title()
            date_list = date.split()
            if not date_list[0] in MONTHS and (len(date_list) > 1 and not date_list[0].isalpha()):
                raise ValueError()

        except ValueError:
            pass

        else:
            if len(date_list) == 1:
                if date_list[0].split("/")[0].isalpha() or int(date_list[0].split("/")[0]) > 12 or int(date_list[0].split("/")[1]) > 31:
                    pass
                else:
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
                if "," in date_list[1]:
                    if int(date_list[1][0:date_list[1].index(",")]) > 31:
                        pass
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
                else:
                    pass



if __name__ == "__main__":
    main()
