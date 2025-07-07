def main():
    user_input = input()
    input_list = user_input.split()
    output_list = []
    
    for x in input_list:
        if x == ":)" :
            output_list.append("\U0001F642")
        elif x == ":(" :
            output_list.append("\U0001F641")
        else:
            output_list.append(x)

    final = " ".join(output_list)
    print(final)

if __name__ == "__main__":
    main()
