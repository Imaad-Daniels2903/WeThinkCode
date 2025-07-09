
def main():
    vowels = "aeiouAEIOU"
    user_input = input("Input: ")
    output_list = []
    for letter in user_input:
        if letter not in vowels:
            output_list.append(letter)
        else:
            continue

    output = "".join(output_list).strip()
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
