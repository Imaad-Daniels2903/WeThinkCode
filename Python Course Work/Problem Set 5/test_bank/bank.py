def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")

def value(greeting):
        if "hello" in greeting:
            return 0
        else:
            if greeting[0] == "h":
                return 20

            else:
                return 100

if __name__ == "__main__":
    main()
