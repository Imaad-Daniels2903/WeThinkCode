import sys

def main():
        user_input = input("Input: ").strip()
        output = shorten(user_input)
        print(f"Output: {output}")


def shorten(word):
    vowels = "aeiouAEIOU"
    output_list = []
    for letter in word:
        if letter not in vowels:
            output_list.append(letter)
        else:
            continue

    return "".join(output_list).strip()



if __name__ == "__main__":
    main()
