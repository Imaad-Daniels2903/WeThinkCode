def main():
    inputted_time = input("What time is it? ").strip()
    converted_time = convert(inputted_time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")

    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")

    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

    else:
        print("")


def convert(time):
    time_split = time.split(":")
    hrs = float(time_split[0])
    mins = float(time_split[-1]) / 60
    full_time = hrs + mins

    return full_time


if __name__ == "__main__":
    main()
