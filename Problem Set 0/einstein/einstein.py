def main():
    user_input = input("m: ")
    m = int(user_input)
    c = 300_000_000
    E = m * (c ** 2)
    print(f"E: {E}")

if __name__ == "__main__":
    main()
