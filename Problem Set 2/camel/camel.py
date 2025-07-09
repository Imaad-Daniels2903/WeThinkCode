def main():
    camelCase = input("camelCase: ")
    camelCase_list = list(camelCase)
    snakeCase_list =[]
    for x in range(len(camelCase_list)):
        if camelCase_list[x].isupper():
            snakeCase_list.append("_")
            snakeCase_list.append(camelCase_list[x].lower())
        else:
            snakeCase_list.append(camelCase_list[x])

    snake_case = "".join(snakeCase_list)
    print(f"snake_case: {snake_case}")

if __name__ == "__main__":
    main()
