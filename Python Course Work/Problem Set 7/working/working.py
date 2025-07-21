import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"(?P<time1>(?P<hrs1>[1-9]|0\d|1[0-2])(:(?P<mins1>[0-5]\d))? (?P<tod1>AM|PM)) to (?P<time2>(?P<hrs2>[1-9]|0\d|1[0-2])(:(?P<mins2>[0-5]\d))? (?P<tod2>AM|PM))", s, re.IGNORECASE):
        times = []
        new_time = ""
        for x in range(1,3):
           
           hrs = match.group("hrs" + str(x))
           if len(hrs) == 1:
               hrs = f"0{hrs}"
           mins = match.group("mins" + str(x))
           if mins == None:
               mins = "00"

           if match.group("tod"+str(x)).upper() == "PM":
                if hrs == "12":
                    new_time = f"{hrs}:{mins}"

                else:
                    new_time = f"{str(int(hrs) + 12)}:{mins}"

           else:
               if hrs == "12":
                   new_time = f"00:{mins}"

               else:
                   new_time = f"{hrs}:{mins}"


           times.append(new_time)

        return " to ".join(times)





    else:
        raise ValueError




if __name__ == "__main__":
    main()
