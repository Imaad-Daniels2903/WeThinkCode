def main():
    greeting = input("Greeting: ").strip().lower()
    match greeting:

        case "hey" | "how you doing?" | "how's it going" :
            print("$20")

        case "what's happening?" | "what's up?" :
            print("$100")

        case _:
            print("$0")

if __name__ == "__main__":
    main()
