import sys
import pyfiglet
import random


def main():
    user_args = sys.argv
    if len(user_args) == 3 and user_args[1] in ["-f", "--font"]:
        fonts = pyfiglet.Figlet().getFonts()
        if not user_args[2] in fonts:
            sys.exit("invalid font")

        else:
            user_input = input("Input: ")
            figlet_output = pyfiglet.figlet_format(user_input, user_args[2])
            print(figlet_output)

    elif len(user_args) == 1:
        user_input = input("Input: ")
        figlet = pyfiglet.Figlet()
        random_font = random.choice(figlet.getFonts())
        figlet_output = pyfiglet.figlet_format(user_input, random_font)
        print(figlet_output)

    else:
        sys.exit("invalid input")



if __name__ == "__main__":
    main()
