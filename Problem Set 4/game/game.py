
import random

def main():
    level = int(input("Level: ").strip())
    winning_val = random.randint(1, level)
    while True:
        try:
            user_guess = int(input("Guess: ").strip())
            if user_guess <= 0:
                raise ValueError()

        except ValueError:
            pass

        else:
            if user_guess > winning_val:
                print("Too large!")
                pass

            elif user_guess < winning_val:
                print("Too small!")
                pass

            else:
                print("Just right!")
                break

if __name__ == "__main__":
    main()
